from dataclasses import dataclass
from typing import Optional


@dataclass(eq=True)
class OpenAlexData:
    title: str
    doi: str
    publication_year: int
    type: str
    is_open_access: bool
    primary_topic: str
    journal: Optional[str]
    publisher: Optional[str]
    cited_by_count: Optional[int]
    fwci: Optional[float]
    citation_normalized_percentile: Optional[str]
