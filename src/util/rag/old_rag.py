import os
import ast
import re
import torch
import subprocess
from dataclasses import dataclass
import os
import ast
import re
import torch
import subprocess
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFacePipeline
from langchain_chroma import Chroma
from langchain_nomic import NomicEmbeddings

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

import urllib.request
from bs4 import BeautifulSoup  # pip install beautifulsoup4

# ============================================================
# 0) MULTI-REPO SPEC (NEW)
# ============================================================

@dataclass(frozen=True)
class RepoSpec:
    """
    Define repos here.

    - repo_id: short stable id used to namespace paths, e.g. "codetiming"
    - repo_root: where the repo lives locally after cloning (or already exists)
    - git_url: optional. if provided, we auto-clone/pull into repo_root
    - persist_directory: where Chroma index for this repo is stored
    """
    repo_id: str
    repo_root: str
    persist_directory: str
    git_url: Optional[str] = None
    docs_urls: Tuple[str, ...] = ()


def ensure_repo_local(spec: RepoSpec) -> str:
    """
    If spec.git_url is set:
      - clone if repo_root doesn't exist
      - else pull latest
    If not set:
      - assumes repo_root already exists locally.
    """
    repo_root = os.path.abspath(spec.repo_root)

    if spec.git_url:
        if not os.path.isdir(repo_root) or not os.path.isdir(os.path.join(repo_root, ".git")):
            os.makedirs(os.path.dirname(repo_root), exist_ok=True)
            print(f"Cloning {spec.repo_id} from {spec.git_url} -> {repo_root}")
            subprocess.check_call(["git", "clone", spec.git_url, repo_root])
        else:
            print(f"Pulling latest for {spec.repo_id} in {repo_root}")
            subprocess.check_call(["git", "-C", repo_root, "pull", "--ff-only"])

    if not os.path.isdir(repo_root):
        raise FileNotFoundError(f"Repo root not found: {repo_root}")

    return repo_root


# ============================================================
# 1) LLM LOADING
# ============================================================

def load_llm(model_id: str = "meta-llama/Llama-3.2-3B-Instruct") -> HuggingFacePipeline:
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    tokenizer = AutoTokenizer.from_pretrained(model_id, token=token)

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        token=token,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )

    if torch.cuda.is_available():
        model = model.to("cuda")

    gen_pipe = pipeline(
        task="text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=600,
        do_sample=False,
        temperature=0.0,
        return_full_text=False,
        device=0 if torch.cuda.is_available() else -1,
    )
    return HuggingFacePipeline(pipeline=gen_pipe)



# ============================================================
# 2) EMBEDDINGS (Nomic v1.5 Implementation)
# ============================================================

def load_embeddings() -> NomicEmbeddings:
    """
    Initializes Nomic Embeddings.
    NOTE: Ensure os.environ["NOMIC_API_KEY"] is set before calling this.
    """
    return NomicEmbeddings(
        model="nomic-embed-text-v1.5",
        dimensionality=768
    )


# ============================================================
# 3) REPO INGESTION (UPDATED: repo_id + namespacing)
# ============================================================

@dataclass
class IngestedFile:
    repo_id: str   # NEW
    path: str      # now namespaced: "<repo_id>:<rel_path>"
    text: str
    kind: str


def _read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1", errors="ignore") as f:
            return f.read()


def ingest_repository(
    repo_root: str,
    repo_id: str,  # NEW
    include_ext: Tuple[str, ...] = (".py", ".md", ".rst", ".txt"),
    exclude_dirs: Tuple[str, ...] = (".git", ".venv", "venv", "__pycache__", "dist", "build", ".mypy_cache"),
) -> List[IngestedFile]:
    """
    Walks the repo and prepares files with the 'search_document:' prefix
    required by Nomic for indexing.

    IMPORTANT MULTI-REPO CHANGE:
    - All file paths are namespaced as: "<repo_id>:<relative_path>"
      so multiple repos can coexist without collisions.
    """
    repo_root = os.path.abspath(repo_root)
    out: List[IngestedFile] = []

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for name in files:
            p = os.path.join(root, name)
            ext = os.path.splitext(name)[1].lower()
            if ext not in include_ext:
                continue

            text = _read_text_file(p).strip()
            if not text:
                continue

            kind = "code" if ext == ".py" else "doc"
            rel_path = os.path.relpath(p, repo_root)

            # MULTI-REPO: namespace the path
            scoped_path = f"{repo_id}:{rel_path}"

            wrapped = f"search_document: FILE: {scoped_path}\nKIND: {kind}\n\n{text}"
            out.append(IngestedFile(repo_id=repo_id, path=scoped_path, text=wrapped, kind=kind))

    print(f"Ingested {len(out)} files from {repo_id} at {repo_root}")
    return out

# For the text documenation URLs
def ingest_doc_urls(repo_id: str, urls: Tuple[str, ...]) -> List[IngestedFile]:
    docs: List[IngestedFile] = []

    for i, url in enumerate(urls, start=1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                html = resp.read().decode("utf-8", errors="ignore")

            soup = BeautifulSoup(html, "html.parser")
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()
            text = soup.get_text("\n").strip()
            if not text:
                continue

            virtual_path = f"{repo_id}:DOC_URL:{i}"
            wrapped = (
                f"search_document: FILE: {virtual_path}\n"
                f"KIND: doc\n"
                f"SOURCE_URL: {url}\n\n"
                f"{text}"
            )

            docs.append(IngestedFile(repo_id=repo_id, path=virtual_path, text=wrapped, kind="doc"))

        except Exception as e:
            print(f"[WARN] Failed to ingest docs from {url}: {e}")

    return docs

# ============================================================
# 4) STRUCTURE-AWARE CHUNKING (Python AST-based)
# ============================================================

def _strip_nomic_wrapper(file_text: str) -> Tuple[str, str]:
    parts = re.split(r"\n\s*\n", file_text, maxsplit=1)
    if len(parts) == 2 and parts[0].lstrip().startswith("search_document:"):
        return parts[0].strip(), parts[1]
    return "", file_text


def _safe_get_source_segment(lines: List[str], start_line: int, end_line: int) -> str:
    start_idx = max(start_line - 1, 0)
    end_idx = min(end_line, len(lines))
    return "".join(lines[start_idx:end_idx]).rstrip() + "\n"


def _build_python_header_chunk(tree: ast.AST, content_lines: List[str]) -> Tuple[int, int]:
    start_line = 1
    end_line = 1

    module_body = getattr(tree, "body", [])
    if not module_body:
        return start_line, len(content_lines)

    i = 0
    if (
        isinstance(module_body[0], ast.Expr)
        and isinstance(getattr(module_body[0], "value", None), (ast.Str, ast.Constant))
        and isinstance(getattr(module_body[0].value, "value", None), str)
        and hasattr(module_body[0], "lineno")
        and hasattr(module_body[0], "end_lineno")
    ):
        end_line = max(end_line, module_body[0].end_lineno)
        i = 1

    for node in module_body[i:]:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            break
        if hasattr(node, "lineno") and hasattr(node, "end_lineno"):
            end_line = max(end_line, node.end_lineno)

    end_line = min(end_line, len(content_lines))
    return start_line, end_line


def _fallback_split_large_chunk(
    base_doc: Document,
    splitter: RecursiveCharacterTextSplitter,
    max_chars: int = 5000,
) -> List[Document]:
    if len(base_doc.page_content) <= max_chars:
        return [base_doc]

    sub_docs = splitter.create_documents([base_doc.page_content], metadatas=[base_doc.metadata])
    out = []
    for idx, d in enumerate(sub_docs, start=1):
        md = dict(d.metadata)
        md["part"] = idx
        md["parts_total"] = len(sub_docs)
        out.append(Document(page_content=d.page_content, metadata=md))
    return out


def build_chunks(files: List[IngestedFile]):
    fallback_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
    )

    docs: List[Document] = []

    for f in files:
        if not f.path.lower().endswith(".py") or f.kind != "code":
            dlist = fallback_splitter.create_documents(
                texts=[f.text],
                metadatas=[{
                    "repo_id": f.repo_id,      # NEW
                    "path": f.path,
                    "kind": f.kind,
                    "chunk_type": "doc"
                }],
            )
            docs.extend(dlist)
            continue

        wrapper_header, content = _strip_nomic_wrapper(f.text)
        content_lines = content.splitlines(keepends=True)

        if not content.strip():
            continue

        try:
            tree = ast.parse(content)
        except SyntaxError:
            dlist = fallback_splitter.create_documents(
                texts=[f.text],
                metadatas=[{
                    "repo_id": f.repo_id,      # NEW
                    "path": f.path,
                    "kind": f.kind,
                    "chunk_type": "python_fallback"
                }],
            )
            docs.extend(dlist)
            continue

        # --------- 1) Header chunk ----------
        h_start, h_end = _build_python_header_chunk(tree, content_lines)
        header_src = _safe_get_source_segment(content_lines, h_start, h_end)

        header_text = (
            (wrapper_header + "\n\n" if wrapper_header else "")
            + f"# CHUNK_TYPE: header\n# FILE: {f.path}\n\n"
            + header_src
        )
        header_doc = Document(
            page_content=header_text,
            metadata={
                "repo_id": f.repo_id,   # NEW
                "path": f.path,
                "kind": f.kind,
                "chunk_type": "header",
                "symbol": "__module__",
                "start_line": h_start,
                "end_line": h_end,
            },
        )
        docs.extend(_fallback_split_large_chunk(header_doc, fallback_splitter))

        # --------- 2) Symbol chunks ----------
        for node in getattr(tree, "body", []):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                symbol = node.name
                if not (hasattr(node, "lineno") and hasattr(node, "end_lineno")):
                    continue
                src = _safe_get_source_segment(content_lines, node.lineno, node.end_lineno)

                chunk_text = (
                    (wrapper_header + "\n\n" if wrapper_header else "")
                    + f"# CHUNK_TYPE: function\n# SYMBOL: {symbol}\n# FILE: {f.path}\n\n"
                    + src
                )
                d = Document(
                    page_content=chunk_text,
                    metadata={
                        "repo_id": f.repo_id,   # NEW
                        "path": f.path,
                        "kind": f.kind,
                        "chunk_type": "function",
                        "symbol": symbol,
                        "start_line": node.lineno,
                        "end_line": node.end_lineno,
                    },
                )
                docs.extend(_fallback_split_large_chunk(d, fallback_splitter))
                continue

            if isinstance(node, ast.ClassDef):
                class_name = node.name
                if not (hasattr(node, "lineno") and hasattr(node, "end_lineno")):
                    continue

                class_src = _safe_get_source_segment(content_lines, node.lineno, node.end_lineno)
                class_text = (
                    (wrapper_header + "\n\n" if wrapper_header else "")
                    + f"# CHUNK_TYPE: class\n# SYMBOL: {class_name}\n# FILE: {f.path}\n\n"
                    + class_src
                )
                class_doc = Document(
                    page_content=class_text,
                    metadata={
                        "repo_id": f.repo_id,   # NEW
                        "path": f.path,
                        "kind": f.kind,
                        "chunk_type": "class",
                        "symbol": class_name,
                        "start_line": node.lineno,
                        "end_line": node.end_lineno,
                    },
                )
                docs.extend(_fallback_split_large_chunk(class_doc, fallback_splitter))

                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if not (hasattr(item, "lineno") and hasattr(item, "end_lineno")):
                            continue
                        method_symbol = f"{class_name}.{item.name}"
                        method_src = _safe_get_source_segment(content_lines, item.lineno, item.end_lineno)

                        method_text = (
                            (wrapper_header + "\n\n" if wrapper_header else "")
                            + f"# CHUNK_TYPE: method\n# SYMBOL: {method_symbol}\n# FILE: {f.path}\n\n"
                            + method_src
                        )
                        method_doc = Document(
                            page_content=method_text,
                            metadata={
                                "repo_id": f.repo_id,   # NEW
                                "path": f.path,
                                "kind": f.kind,
                                "chunk_type": "method",
                                "symbol": method_symbol,
                                "start_line": item.lineno,
                                "end_line": item.end_lineno,
                            },
                        )
                        docs.extend(_fallback_split_large_chunk(method_doc, fallback_splitter))

    print(f"Created {len(docs)} chunks (structure-aware)")
    return docs


def build_or_load_vector_store(chunks, embeddings, persist_directory="chroma_repo_index") -> Chroma:
    if os.path.isdir(persist_directory) and os.listdir(persist_directory):
        print(f"Loading existing Chroma DB from {persist_directory}")
        return Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    print(f"Building new Chroma DB in {persist_directory}")
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
    )




def format_docs(docs) -> str:
    return "\n\n---\n\n".join(d.page_content for d in docs)


def preview_chunks(chunks: List[Document], n: int = 5) -> None:
    print("\n" + "=" * 80)
    print(f"PREVIEWING {min(n, len(chunks))} / {len(chunks)} CHUNKS")
    print("=" * 80)

    for i, d in enumerate(chunks[:n], start=1):
        print(f"\n--- CHUNK {i} ---")
        print("METADATA:", d.metadata)
        print("CONTENT (first 600 chars):")
        print(d.page_content[:600])

def preview_first_code_chunk(chunks):
    for d in chunks:
        if d.metadata.get("chunk_type") in ("header", "function", "class", "method"):
            print("\nFIRST CODE CHUNK FOUND")
            print("METADATA:", d.metadata)
            print(d.page_content[:800])
            return
    print("No code chunks found.")

# ============================================================
# 5) RAG CHAIN FOR TEST READABILITY REFACTORING
# ============================================================

def build_test_refactor_rag_chain(llm, vector_store, k: int = 8):
    retriever = vector_store.as_retriever(search_kwargs={"k": k})

    def retrieval_query(x: dict) -> str:
        test_code = x["test_code"]
        module_hint = x.get("module_hint", "")
        extra_hint = x.get("extra_hint", "")
        snippet = test_code[:1200]
        return f"search_query: {module_hint} {extra_hint}\n\n{snippet}".strip()

    prompt = ChatPromptTemplate.from_template(
        """You are refactoring AUTOMATICALLY GENERATED pytest tests to improve readability.

You will receive:
1) Retrieved repository context (source code + docs)
2) The generated test code that MUST keep the same behavior

REPO CONTEXT (use this to avoid hallucinations):
<context>
{context}
</context>

GENERATED TEST CODE (do not change semantics):
<test>
{test_code}
</test>

STRICT RULES:
- Preserve semantics: do not change assertions meaning, test logic, or side effects.
- Do NOT add new functionality. Do NOT "fix" the system under test.
- You MAY: rename variables, extract helpers, add comments, improve naming.
- Keep imports correct.
- Output ONLY the complete refactored test code (no explanations).

Refactored test code:
"""
    )

    rag_inputs = RunnableParallel(
        context=(lambda x: retrieval_query(x)) | retriever | format_docs,
        test_code=lambda x: x["test_code"],
    )

    chain = rag_inputs | prompt | llm | StrOutputParser()
    return chain


# ============================================================
# 6) MULTI-REPO DRIVER (NEW)
# ============================================================

def build_indexes_for_repos(repos: List[RepoSpec]) -> Dict[str, Chroma]:
    """
    Automates ingestion/chunking/indexing for many repos.
    Returns {repo_id: vector_store}.
    """
    embeddings = load_embeddings()
    vectorstores: Dict[str, Chroma] = {}

    for spec in repos:
        repo_root = ensure_repo_local(spec)

        files = ingest_repository(repo_root=repo_root, repo_id=spec.repo_id)
        # add docs from URLs
        if spec.docs_urls:
            doc_files = ingest_doc_urls(spec.repo_id, spec.docs_urls)
            print(f"Ingested {len(doc_files)} external docs for {spec.repo_id}")
            files.extend(doc_files)
        chunks = build_chunks(files)
        # Debug preview
        preview_chunks(chunks, n=15)
        preview_first_code_chunk(chunks)
        vector_store = build_or_load_vector_store(
            chunks=chunks,
            embeddings=embeddings,
            persist_directory=spec.persist_directory,
        )
        vectorstores[spec.repo_id] = vector_store

    return vectorstores


# ============================================================
# 7) EXAMPLE MAIN
# ============================================================

if __name__ == "__main__":
    # Ensure you have set your API keys:
    # os.environ["NOMIC_API_KEY"] = "..."
    # os.environ["HUGGINGFACEHUB_API_TOKEN"] = "..."

    # ✅ THIS is where you “give the repos”:
    REPOS: List[RepoSpec] = [
        RepoSpec(
            repo_id="codetiming",
            git_url="https://github.com/realpython/codetiming.git",
            repo_root="./repos/codetiming",
            persist_directory="./chroma_indexes/codetiming",
            docs_urls=("https://pypi.org/project/codetiming/",),
        ),
        # Add the rest here (up to 19):
        # RepoSpec(repo_id="repo2", git_url="https://github.com/...", repo_root="./repos/repo2", persist_directory="./chroma_indexes/repo2"),
    ]

    vectorstores = build_indexes_for_repos(REPOS)

    # Use ONE repo’s vector store for a run (example: codetiming)
    vector_store = vectorstores["codetiming"]

    llm = load_llm()
    rag_refactor = build_test_refactor_rag_chain(llm, vector_store, k=8)

    generated_test_code = """
import pytest
from codetiming import Timer

def test_something():
    t = Timer()
    t.start()
    t.stop()
    assert t.last > 0
"""

    result = rag_refactor.invoke({
        "test_code": generated_test_code,
        "module_hint": "codetiming timer logic",
        "extra_hint": "standard pytest structure",
    })

    print("-" * 30)
    print("REFACTORED TEST CODE:")
    print("-" * 30)
    print(result)