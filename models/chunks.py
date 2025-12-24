from numpy import ndarray
from dataclasses import dataclass


@dataclass(eq=True)
class Chunk:
    chunk_type: str
    page_no: int
    content: str
    embedding: ndarray
