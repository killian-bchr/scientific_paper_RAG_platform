from datetime import date
from typing import List, Optional

from pydantic import BaseModel

from backend.schemas.author import Author
from backend.schemas.category import Category
from backend.schemas.domain import Domain


class PaperBase(BaseModel):
    id: int
    arxiv_id: str
    title: str
    pdf_url: str
    abstract: str
    publication_date: date
    doi: Optional[str]
    journal: Optional[str]
    publisher: Optional[str]
    cited_by_count: Optional[int]
    fwci: Optional[float]
    citation_normalized_percentile: Optional[float]
    reliability_score: float

    class Config:
        from_attributes = True


class PaperList(PaperBase):
    pass


class PaperDetail(PaperBase):
    authors: List[Author]
    domains: List[Domain]
    categories: List[Category]
