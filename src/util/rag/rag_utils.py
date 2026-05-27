import os
import ast
import re
from typing import List, Tuple

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_nomic import NomicEmbeddings

from bs4 import BeautifulSoup
import urllib.request
from dataclasses import dataclass


# ============================================================
# DATA STRUCTURES
# ============================================================

@dataclass
class IngestedFile:
    repo_id: str
    path: str
    text: str
    kind: str


# ============================================================
# EMBEDDINGS
# ============================================================

def load_embeddings() -> NomicEmbeddings:
    return NomicEmbeddings(
        model="nomic-embed-text-v1.5",
        dimensionality=768,
    )


# ============================================================
# INGESTION
# ============================================================

def _read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1", errors="ignore") as f:
            return f.read()


def ingest_repository(
    repo_root: str,
    repo_id: str,
    include_ext: Tuple[str, ...] = (".py", ".md", ".rst", ".txt"),
    exclude_dirs: Tuple[str, ...] = (
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "dist",
        "build",
    ),
):

    out: List[IngestedFile] = []
    repo_root = os.path.abspath(repo_root)

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext not in include_ext:
                continue

            p = os.path.join(root, name)
            text = _read_text_file(p).strip()
            if not text:
                continue

            rel_path = os.path.relpath(p, repo_root)
            scoped_path = f"{repo_id}:{rel_path}"
            kind = "code" if ext == ".py" else "doc"

            wrapped = (
                f"search_document: FILE: {scoped_path}\n"
                f"KIND: {kind}\n\n{text}"
            )

            out.append(
                IngestedFile(
                    repo_id=repo_id,
                    path=scoped_path,
                    text=wrapped,
                    kind=kind,
                )
            )

    return out


def ingest_doc_urls(repo_id: str, urls: Tuple[str, ...]):
    docs = []

    for i, url in enumerate(urls, start=1):
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="ignore")

        soup = BeautifulSoup(html, "html.parser")
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text("\n").strip()
        if not text:
            continue

        wrapped = (
            f"search_document: FILE: {repo_id}:DOC_URL:{i}\n"
            f"KIND: doc\n"
            f"SOURCE_URL: {url}\n\n{text}"
        )
        docs.append(
            IngestedFile(
                repo_id=repo_id,
                path=f"{repo_id}:DOC_URL:{i}",
                text=wrapped,
                kind="doc",
            )
        )

    return docs


# ============================================================
# CHUNKING
# ============================================================

def build_chunks(files):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
    )

    docs: List[Document] = []

    for f in files:
        docs.extend(
            splitter.create_documents(
                texts=[f.text],
                metadatas=[{
                    "repo_id": f.repo_id,
                    "path": f.path,
                    "kind": f.kind,
                }],
            )
        )

    return docs


# ============================================================
# VECTOR STORE
# ============================================================

def build_or_load_vector_store(
    chunks,
    embeddings,
    persist_directory: str,
) -> Chroma:
    if os.path.isdir(persist_directory) and os.listdir(persist_directory):
        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings,
        )

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory,
    )
