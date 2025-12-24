from dataclasses import dataclass


@dataclass(eq=True)
class Domain:
    name: str
