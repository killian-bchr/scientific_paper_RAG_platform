from abc import ABC, abstractmethod
from typing import List

from backend.database.tables import PaperORM


class BaseRetriever(ABC):
    def __init__(self, papers: List[PaperORM]):
        self.papers = papers
        self.paper_ids = [p.id for p in papers]
        self.papers_by_id = {p.id: p for p in papers}
        self.is_empty = len(papers) == 0

    @abstractmethod
    def retrieve(self):
        pass
