# chunking.py
from __future__ import annotations

import ast
import re
from typing import List, Tuple

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def _strip_nomic_wrapper(file_text: str) -> Tuple[str, str]:
    parts = re.split(r"\n\s*\n", file_text, maxsplit=1)
    if len(parts) == 2 and parts[0].lstrip().startswith("search_document:"):
        return parts[0].strip(), parts[1]
    return "", file_text


def _wrap_with_nomic_header(repo_id: str, path: str, kind: str, body: str, source_url: str = None) -> str:
    header = f"search_document: FILE: {path}\nKIND: {kind}"
    if source_url:
        header += f"\nSOURCE_URL: {source_url}"
    return header + "\n\n" + body


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
        and isinstance(getattr(module_body[0], "value", None), ast.Constant)
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
    out: List[Document] = []

    for idx, d in enumerate(sub_docs, start=1):
        md = dict(d.metadata)
        md["part"] = idx
        md["parts_total"] = len(sub_docs)

        _, body = _strip_nomic_wrapper(d.page_content)

        wrapped = _wrap_with_nomic_header(
            repo_id=md.get("repo_id", ""),
            path=md.get("path", ""),
            kind=md.get("kind", ""),
            body=body,
        )
        out.append(Document(page_content=wrapped, metadata=md))

    return out


def build_chunks(files):
    """
    files must have: .repo_id, .path, .text, .kind
    (your IngestedFile fits this)
    """
    fallback_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
    )

    docs: List[Document] = []

    for f in files:
        if not f.path.lower().endswith(".py") or f.kind != "code":
            _, body = _strip_nomic_wrapper(f.text)
            parts = fallback_splitter.split_text(body)
            for idx, part in enumerate(parts, start=1):
                wrapped_part = _wrap_with_nomic_header(f.repo_id, f.path, f.kind, part)
                docs.append(Document(
                    page_content=wrapped_part,
                    metadata={
                        "repo_id": f.repo_id,
                        "path": f.path,
                        "kind": f.kind,
                        "chunk_type": "doc",
                        "part": idx,
                        "parts_total": len(parts),
                    },
                ))
            continue

        wrapper_header, content = _strip_nomic_wrapper(f.text)
        content_lines = content.splitlines(keepends=True)

        if not content.strip():
            continue

        try:
            tree = ast.parse(content)
        except SyntaxError:
            _, body = _strip_nomic_wrapper(f.text)
            parts = fallback_splitter.split_text(body)
            for idx, part in enumerate(parts, start=1):
                wrapped_part = _wrap_with_nomic_header(f.repo_id, f.path, f.kind, part)
                docs.append(Document(
                    page_content=wrapped_part,
                    metadata={
                        "repo_id": f.repo_id,
                        "path": f.path,
                        "kind": f.kind,
                        "chunk_type": "python_fallback",
                        "part": idx,
                        "parts_total": len(parts),
                    },
                ))
            continue

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
                "repo_id": f.repo_id,
                "path": f.path,
                "kind": f.kind,
                "chunk_type": "header",
                "symbol": "__module__",
                "start_line": h_start,
                "end_line": h_end,
            },
        )
        docs.extend(_fallback_split_large_chunk(header_doc, fallback_splitter))

        for node in getattr(tree, "body", []):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if not (hasattr(node, "lineno") and hasattr(node, "end_lineno")):
                    continue
                src = _safe_get_source_segment(content_lines, node.lineno, node.end_lineno)

                chunk_text = (
                    (wrapper_header + "\n\n" if wrapper_header else "")
                    + f"# CHUNK_TYPE: function\n# SYMBOL: {node.name}\n# FILE: {f.path}\n\n"
                    + src
                )
                d = Document(
                    page_content=chunk_text,
                    metadata={
                        "repo_id": f.repo_id,
                        "path": f.path,
                        "kind": f.kind,
                        "chunk_type": "function",
                        "symbol": node.name,
                        "start_line": node.lineno,
                        "end_line": node.end_lineno,
                    },
                )
                docs.extend(_fallback_split_large_chunk(d, fallback_splitter))
                continue

            if isinstance(node, ast.ClassDef):
                if not (hasattr(node, "lineno") and hasattr(node, "end_lineno")):
                    continue
                class_name = node.name
                class_src = _safe_get_source_segment(content_lines, node.lineno, node.end_lineno)

                class_text = (
                    (wrapper_header + "\n\n" if wrapper_header else "")
                    + f"# CHUNK_TYPE: class\n# SYMBOL: {class_name}\n# FILE: {f.path}\n\n"
                    + class_src
                )
                class_doc = Document(
                    page_content=class_text,
                    metadata={
                        "repo_id": f.repo_id,
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
                                "repo_id": f.repo_id,
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

def validate_chunks(chunks: List[Document]) -> None:
    bad = [d for d in chunks if not d.page_content.lstrip().startswith("search_document:")]
    print(f"Chunks missing Nomic header: {len(bad)}")
    if bad:
        print("Example bad chunk path:", bad[0].metadata.get("path"))