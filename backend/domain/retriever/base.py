from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from backend.database.tables import PaperORM


class BaseRetriever(ABC):
    def __init__(self, papers: List[PaperORM]):
        self.papers = papers
        self.paper_ids = [p.id for p in papers]
        self.papers_by_id = {p.id: p for p in papers}
        self.is_empty = len(papers) == 0

    @abstractmethod
    def compute_scores(self, query: str) -> Dict[int, float]:
        pass

    def top_k_papers_ids(self, query: str, k: int) -> List[int]:
        scores = self.compute_scores(query)
        return sorted(scores, key=scores.get, reverse=True)[:k]

    def retrieve_top_papers_with_scores(
        self,
        query: str,
        k: int = 10,
    ) -> List[Tuple[PaperORM, float]]:
        scores = self.compute_scores(query)

        results = []
        for paper_id, score in scores.items():
            paper = self.papers_by_id.get(paper_id)
            if paper:
                results.append((paper, score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:k]

    def retrieve_top_papers(
        self,
        query: str,
        k: int = 10,
    ) -> List[PaperORM]:
        results_with_scores = self.retrieve_top_papers_with_scores(query, k)
        return [paper for paper, _ in results_with_scores]
