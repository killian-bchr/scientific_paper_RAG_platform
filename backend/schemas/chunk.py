from pydantic import BaseModel


class Chunk(BaseModel):
    id: int
    paper_id: int
    chunk_type: str
    page_no: int
    content: str

    class Config:
        from_attributes = True
