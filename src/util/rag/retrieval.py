# retrieval.py
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence

from langchain_chroma import Chroma
from langchain_core.documents import Document

IMPORT_RE = re.compile(
    r"^\s*(?:from\s+([a-zA-Z0-9_\.]+)\s+import\s+(.+)|import\s+(.+))",
    re.M,
)

COMMON_BEHAVIOR_WORDS = [
    "start", "stop", "last", "elapsed", "timer",
    "exception", "error", "raises", "fixture", "mock",
]


def extract_import_terms(test_code: str) -> List[str]:
    terms: List[str] = []
    for m in IMPORT_RE.finditer(test_code):
        frm, imp, imp2 = m.group(1), m.group(2), m.group(3)
        if frm:
            terms.append(frm.split(".")[0])
        if imp:
            for t in imp.split(","):
                t = t.strip().split(" ")[0]
                if t and t != "*":
                    terms.append(t)
        if imp2:
            for t in imp2.split(","):
                t = t.strip().split(" ")[0]
                if t:
                    terms.append(t.split(".")[0])

    seen = set()
    out: List[str] = []
    for t in terms:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def infer_restrict_repos(
    vectorstores: Dict[str, Chroma],
    test_code: str,
    module_hint: str = "",
) -> Optional[List[str]]:
    """
    If the test imports (or module_hint mentions) something that matches a repo_id,
    restrict retrieval to only those repos.

    Example: repo_id="codetiming" and test contains "from codetiming import Timer"
    -> restrict_repos=["codetiming"]
    """
    repo_ids = list(vectorstores.keys())

    # candidates from imports and module_hint
    terms = extract_import_terms(test_code)
    hint_terms = re.findall(r"[a-zA-Z_][a-zA-Z0-9_\-]*", (module_hint or "").lower())

    candidates = {t.lower() for t in terms} | {t.lower() for t in hint_terms}

    matched = [rid for rid in repo_ids if rid.lower() in candidates]
    return matched or None


def build_retrieval_queries(
    test_code: str,
    module_hint: str = "",
    extra_hint: str = "",
    snippet_chars: int = 600,
) -> List[str]:
    imports = extract_import_terms(test_code)
    imports_q = " ".join(imports)

    behavior = [w for w in COMMON_BEHAVIOR_WORDS if w in test_code]
    snippet = test_code[:snippet_chars]

    queries: List[str] = []
    if module_hint.strip():
        queries.append(module_hint.strip())
    if imports_q.strip():
        queries.append(f"{module_hint} {imports_q}".strip())
    if behavior:
        queries.append(f"{module_hint} behavior {' '.join(behavior)}".strip())
    if extra_hint.strip():
        queries.append(f"{module_hint} {extra_hint}".strip())
    if snippet.strip():
        queries.append(snippet.strip())

    seen = set()
    out: List[str] = []
    for q in queries:
        q = q.strip()
        if q and q not in seen:
            seen.add(q)
            out.append(q)
    return out


@dataclass(frozen=True)
class RetrievalConfig:
    search_type: str = "mmr"     # "similarity" or "mmr"
    k_code: int = 8              # candidates per query PER REPO (pooled globally)
    k_docs: int = 2
    fetch_k: int = 40
    lambda_mult: float = 0.4
    snippet_chars: int = 600
    prefer_code: bool = True
    include_docs: bool = True

    # Global caps
    max_code_total: int = 10
    max_docs_total: int = 2
    max_chars_per_doc: int = 1400


def _make_retriever(
    vector_store: Chroma,
    *,
    search_type: str,
    k: int,
    fetch_k: int,
    lambda_mult: float,
    kind_filter: Optional[str] = None,
):
    search_kwargs = {"k": k}
    if search_type == "mmr":
        search_kwargs.update({"fetch_k": fetch_k, "lambda_mult": lambda_mult})
    if kind_filter:
        search_kwargs["filter"] = {"kind": kind_filter}
    return vector_store.as_retriever(search_type=search_type, search_kwargs=search_kwargs)


def dedup_docs(docs: Sequence[Document]) -> List[Document]:
    seen = set()
    out: List[Document] = []
    for d in docs:
        md = d.metadata or {}
        key = (
            md.get("repo_id"),
            md.get("path"),
            md.get("chunk_type"),
            md.get("symbol"),
            d.page_content[:120],
        )
        if key not in seen:
            seen.add(key)
            out.append(d)
    return out


def _keywords(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z_][a-zA-Z0-9_]{2,}", text.lower()))


def keyword_overlap_score(query: str, doc: Document) -> float:
    qk = _keywords(query)
    if not qk:
        return 0.0
    dk = _keywords(doc.page_content[:2000])
    return len(qk & dk) / max(1, len(qk))


def _format_snippet(doc: Document, max_chars: int) -> str:
    md = doc.metadata or {}
    header = (
        f"FILE: {md.get('path')} | kind={md.get('kind')} | "
        f"chunk_type={md.get('chunk_type')} | symbol={md.get('symbol')} | "
        f"lines={md.get('start_line')}-{md.get('end_line')}"
    )
    txt = doc.page_content
    if len(txt) > max_chars:
        txt = txt[:max_chars] + "\n... (truncated)"
    return header + "\n" + txt


def retrieve_documents_multi(
    vectorstores: Dict[str, Chroma],
    test_code: str,
    module_hint: str = "",
    extra_hint: str = "",
    cfg: Optional[RetrievalConfig] = None,
    restrict_repos: Optional[Sequence[str]] = None,
) -> List[Document]:
    cfg = cfg or RetrievalConfig()

    queries = build_retrieval_queries(
        test_code=test_code,
        module_hint=module_hint,
        extra_hint=extra_hint,
        snippet_chars=cfg.snippet_chars,
    )

    # repo routing (only when caller didn't specify restrict_repos)
    if restrict_repos is None:
        inferred = infer_restrict_repos(
            vectorstores=vectorstores,
            test_code=test_code,
            module_hint=module_hint,
        )
        if inferred:
            restrict_repos = inferred

    # Build repo_items AFTER routing decision, then apply filter
    repo_items = list(vectorstores.items())
    if restrict_repos:
        allowed = set(restrict_repos)
        repo_items = [(rid, vs) for rid, vs in repo_items if rid in allowed]

    print(f"[retrieval] restrict_repos={restrict_repos} | searching repos={[rid for rid, _ in repo_items]}")

    code_candidates: List[Document] = []
    doc_candidates: List[Document] = []

    # Collect code candidates
    if cfg.prefer_code:
        for q in queries:
            for repo_id, vs in repo_items:
                ret = _make_retriever(
                    vs,
                    search_type=cfg.search_type,
                    k=cfg.k_code,
                    fetch_k=cfg.fetch_k,
                    lambda_mult=cfg.lambda_mult,
                    kind_filter="code",
                )
                found = ret.invoke(q)
                for d in found:
                    d.metadata = dict(d.metadata or {})
                    d.metadata["repo_id"] = d.metadata.get("repo_id", repo_id)
                code_candidates.extend(found)

    # Collect doc candidates (only first 2 queries)
    if cfg.include_docs:
        for q in queries[:2]:
            for repo_id, vs in repo_items:
                ret = _make_retriever(
                    vs,
                    search_type=cfg.search_type,
                    k=cfg.k_docs,
                    fetch_k=cfg.fetch_k,
                    lambda_mult=cfg.lambda_mult,
                    kind_filter="doc",
                )
                found = ret.invoke(q)
                for d in found:
                    d.metadata = dict(d.metadata or {})
                    d.metadata["repo_id"] = d.metadata.get("repo_id", repo_id)
                doc_candidates.extend(found)

    code_candidates = dedup_docs(code_candidates)
    doc_candidates = dedup_docs(doc_candidates)

    rerank_query = (
        (queries[1] if len(queries) > 1 else queries[0])
        if queries
        else (module_hint or test_code[:300])
    )

    def sort_scored(ds: List[Document]) -> List[Document]:
        scored = [(d, keyword_overlap_score(rerank_query, d)) for d in ds]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [d for d, _ in scored]

    code_top = sort_scored(code_candidates)[: cfg.max_code_total]
    doc_top = sort_scored(doc_candidates)[: cfg.max_docs_total]

    return code_top + doc_top


def retrieve_context_multi(
    vectorstores: Dict[str, Chroma],
    test_code: str,
    tokenizer,
    module_hint: str = "",
    extra_hint: str = "",
    cfg: Optional[RetrievalConfig] = None,
    restrict_repos: Optional[Sequence[str]] = None,
    max_input_tokens: int = 16384,
    reserved_for_generation: int = 800,
) -> str:
    cfg = cfg or RetrievalConfig()

    docs = retrieve_documents_multi(
        vectorstores=vectorstores,
        test_code=test_code,
        module_hint=module_hint,
        extra_hint=extra_hint,
        cfg=cfg,
        restrict_repos=restrict_repos,
    )

    usable = max(512, max_input_tokens - reserved_for_generation)

    parts: List[str] = []
    used = 0

    for d in docs:
        snippet = _format_snippet(d, max_chars=cfg.max_chars_per_doc)
        t = len(tokenizer.encode(snippet, add_special_tokens=False))
        if used + t > usable:
            break
        parts.append(snippet)
        used += t

    return "\n\n---\n\n".join(parts)