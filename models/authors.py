from dataclasses import dataclass


@dataclass(eq=True)
class Author:
    name: str
