from typing import Optional

from pydantic import BaseModel


class Chunk(BaseModel):
    id: int
    paper_id: int
    chunk_type: str
    page_no: int
    content: str
    previous_chunk_id: Optional[int]
    next_chunk_id: Optional[int]

    class Config:
        from_attributes = True
