from pydantic import BaseModel


class Stats(BaseModel):
    total_papers: int
    total_authors: int
    total_domains: int
    total_categories: int
