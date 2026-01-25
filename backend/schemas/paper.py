from datetime import date
from typing import List

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

    class Config:
        from_attributes = True


class PaperList(PaperBase):
    pass


class PaperDetail(PaperBase):
    authors: List[Author]
    domains: List[Domain]
    categories: List[Category]
