from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    paper_id: int
    chunk_id: int
    text: str
    score: float
