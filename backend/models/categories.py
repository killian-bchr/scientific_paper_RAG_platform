from dataclasses import dataclass

from backend.models.domains import Domain


@dataclass(eq=True)
class Category:
    name: str
    domain: Domain
