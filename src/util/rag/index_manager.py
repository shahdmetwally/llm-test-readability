from __future__ import annotations

from typing import Dict, List

from langchain_chroma import Chroma

# Import the new implementation
from .rag_pipeline import build_indexes_for_repos, RepoSpec


class RepoIndexManager:
    """
    Wrapper around rag_pipeline's build_indexes_for_repos.
    Kept for backward compatibility with src/main.py.
    """

    def __init__(self, repos: List[RepoSpec]):
        self.repos = repos
        self.vectorstores: Dict[str, Chroma] = {}

    def build(self) -> Dict[str, Chroma]:
        """
        Builds or loads vector stores for all configured repos using the new pipeline.
        """
        # Delegate directly to the new pipeline
        self.vectorstores = build_indexes_for_repos(self.repos)
        return self.vectorstores
