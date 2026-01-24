from dataclasses import dataclass

from numpy import ndarray


@dataclass(eq=True)
class Chunk:
    chunk_type: str
    page_no: int
    content: str
    embedding: ndarray
