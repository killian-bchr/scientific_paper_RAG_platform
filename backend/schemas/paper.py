from datetime import date

from pydantic import BaseModel


class Paper(BaseModel):
    id: int
    arxiv_id: str
    title: str
    pdf_url: str
    abstract: str
    publication_date: date

    class Config:
        from_attributes = True
