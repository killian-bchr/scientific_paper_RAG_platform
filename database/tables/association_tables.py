from sqlalchemy import Column, Integer, ForeignKey, Table
from database.base import Base


paper_author = Table(
    "paper_author",
    Base.metadata,
    Column("paper_id", ForeignKey("papers.id"), primary_key=True),
    Column("author_id", ForeignKey("authors.id"), primary_key=True),
)

paper_domain = Table(
    "paper_domain",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("papers.id"), primary_key=True),
    Column("domain_id", Integer, ForeignKey("domains.id"), primary_key=True),
)

paper_category = Table(
    "paper_category",
    Base.metadata,
    Column("paper_id", Integer, ForeignKey("papers.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
)
