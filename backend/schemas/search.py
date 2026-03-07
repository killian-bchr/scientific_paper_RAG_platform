from typing import List, Optional

from pydantic import BaseModel

from backend.schemas.chunk import Chunk
from backend.schemas.paper import PaperDetail


class SearchQuery(BaseModel):
    query: str
    domain_id: Optional[int] = None
    category_id: Optional[int] = None
    start_year: Optional[int] = None
    end_year: Optional[int] = None
    top_k_papers: int = 10
    top_k_chunks: int = 10
    chunk_relevance_threshold: float = 0.5


class ChunkResult(BaseModel):
    chunk: Chunk
    score: float


class SearchResult(BaseModel):
    paper: PaperDetail
    score: float
    chunks: List[ChunkResult]
