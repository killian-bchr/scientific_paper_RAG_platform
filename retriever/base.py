from abc import ABC, abstractmethod
from typing import Dict, List

from database.tables import PaperORM


class BaseRetriever(ABC):
    def __init__(self, papers: List[PaperORM]):
        self.papers = papers
        self.paper_ids = [p.id for p in papers]
        self.is_empty = len(papers) == 0

    @abstractmethod
    def compute_scores(self, query: str) -> Dict[int, float]:
        pass

    def top_k_papers(self, query: str, k: int) -> List[int]:
        scores = self.compute_scores(query)
        return sorted(scores, key=scores.get, reverse=True)[:k]

    def retrieve_top_papers(self, query: str, k: int = 10) -> List[PaperORM]:
        top_papers = self.top_k_papers(query, k)
        return [p for p in self.papers if p.id in top_papers]
