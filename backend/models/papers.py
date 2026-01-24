from dataclasses import dataclass
from datetime import date
from typing import List

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
