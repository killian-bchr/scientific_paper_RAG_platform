from typing import Optional

from pydantic import BaseModel

from backend.schemas.paper import PaperDetail


class SearchQuery(BaseModel):
    query: str
    domain_id: Optional[int] = None
    category_id: Optional[int] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    limit: int = 10


class SearchResult(BaseModel):
    paper: PaperDetail
    score: float
    # TODO: return relevant chunks as following : chunks: List[str] = []
