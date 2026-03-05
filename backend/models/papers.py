from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from backend.models import Author, Category, Domain


@dataclass(eq=True)
class Paper:
    arxiv_id: str
    title: str
    pdf_url: str
    abstract: str
    publication_date: date
    authors: List[Author]
    domains: List[Domain]
    categories: List[Category]
    doi: Optional[str]
    journal: Optional[str]
    publisher: Optional[str]
    cited_by_count: Optional[int]
    fwci: Optional[float]
    citation_normalized_percentile: Optional[float]
    reliability_score: float
