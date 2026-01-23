from typing import Any, List

from sqlalchemy.orm import Session

from database.tables import (
    AuthorORM,
    CategoryORM,
    ChunkORM,
    DomainORM,
    PaperORM,
    UserORM,
)
from helpers.utils import Utils
from models import Author, Category, Chunk, Domain, Paper
from settings.constants import UserRole


class CRUD:
    @staticmethod
    def add_object_to_session(session: Session, object: Any):
        session.add(object)

    @staticmethod
    def flush_session(session: Session):
        session.flush()

    @staticmethod
    def flush_object_to_session(session: Session, object: Any):
        CRUD.add_object_to_session(session, object)
        CRUD.flush_session(session)

    @staticmethod
    def user_to_orm(
        session: Session,
        username: str,
        hashed_password: str,
        role: UserRole = UserRole.USER,
        flush: bool = False,
    ) -> UserORM:
        existing_user = Utils.fetch_user_by_username(session, username)
        if existing_user:
            return existing_user

        # TODO: check if Admin role is authorized for correspondind username

        user_orm = UserORM(
            username=username,
            hashed_password=hashed_password,
            role=role.value,
        )

        CRUD.add_object_to_session(session, user_orm)

        if flush:
            CRUD.flush_session(session)

        return user_orm

    @staticmethod
    def author_to_orm(
        session: Session, author: Author, flush: bool = False
    ) -> AuthorORM:
        existing_author = Utils.get_existing_author(session, author.name)
        if existing_author:
            return existing_author

        author_orm = AuthorORM(name=author.name)

        CRUD.add_object_to_session(session, author_orm)

        if flush:
            CRUD.flush_session(session)

        return author_orm

    @staticmethod
    def authors_to_orm(
        session: Session, authors: List[Author], flush: bool = False
    ) -> List[AuthorORM]:
        authors_orm = [CRUD.author_to_orm(session, a) for a in authors]

        if flush:
            CRUD.flush_session(session)

        return authors_orm

    @staticmethod
    def domain_to_orm(
        session: Session, domain: Domain, flush: bool = False
    ) -> DomainORM:
        existing_domain = Utils.get_existing_domain(session, domain.name)
        if existing_domain:
            return existing_domain

        domain_orm = DomainORM(name=domain.name)

        CRUD.add_object_to_session(session, domain_orm)

        if flush:
            CRUD.flush_session(session)

        return domain_orm

    @staticmethod
    def domains_to_orm(
        session: Session, domains: List[Domain], flush: bool = False
    ) -> List[DomainORM]:
        domains_orm = [CRUD.domain_to_orm(session, d) for d in domains]

        if flush:
            CRUD.flush_session(session)

        return domains_orm

    @staticmethod
    def category_to_orm(
        session: Session,
        category: Category,
        flush: bool = False,
    ) -> CategoryORM:
        existing_category = Utils.get_existing_category(
            session, category.name, category.domain.name
        )
        if existing_category:
            return existing_category

        domain_orm = Utils.get_existing_domain(session, category.domain.name)
        if domain_orm is None:
            raise ValueError(
                "The corresponding domain to this category should already exists !"
            )

        category_orm = CategoryORM(name=category.name, domain_id=domain_orm.id)

        CRUD.add_object_to_session(session, category_orm)

        category_orm.domain = domain_orm

        if flush:
            CRUD.flush_session(session)

        return category_orm

    @staticmethod
    def categories_to_orm(
        session: Session,
        categories: List[Category],
        flush: bool = False,
    ) -> List[CategoryORM]:
        categories_orm = [CRUD.category_to_orm(session, c) for c in categories]

        if flush:
            CRUD.flush_session(session)

        return categories_orm

    @staticmethod
    def paper_to_orm(session: Session, paper: Paper, flush: bool = False) -> PaperORM:
        existing_paper = Utils.get_existing_paper(session, paper.arxiv_id)
        if existing_paper:
            return existing_paper

        paper_orm = PaperORM(
            arxiv_id=paper.arxiv_id,
            title=paper.title,
            pdf_url=paper.pdf_url,
            abstract=paper.abstract,
            publication_date=paper.publication_date,
        )

        CRUD.add_object_to_session(session, paper_orm)

        paper_orm.authors = CRUD.authors_to_orm(session, paper.authors)

        paper_orm.domains = CRUD.domains_to_orm(session, paper.domains, flush=True)
        paper_orm.categories = CRUD.categories_to_orm(session, paper.categories)

        if flush:
            CRUD.flush_session(session)

        return paper_orm

    @staticmethod
    def chunk_to_orm(
        session: Session,
        chunk: Chunk,
        paper_orm: PaperORM,
        flush: bool = False,
    ) -> ChunkORM:
        chunk_orm = ChunkORM(
            chunk_type=chunk.chunk_type,
            page_no=chunk.page_no,
            content=chunk.content,
            embedding=chunk.embedding,
        )
        chunk_orm.paper = paper_orm
        CRUD.add_object_to_session(session, chunk_orm)

        if flush:
            CRUD.flush_session(session)

        return chunk_orm

    @staticmethod
    def chunks_to_orm(
        session: Session,
        chunks: List[Chunk],
        paper_orm: PaperORM,
        flush: bool = False,
    ) -> List[ChunkORM]:
        chunks_orm = [CRUD.chunk_to_orm(session, c, paper_orm) for c in chunks]

        if flush:
            CRUD.flush_session(session)

        return chunks_orm

    @staticmethod
    def save_complete_paper(session: Session, paper: Paper, flush: bool = True) -> None:
        # TODO: write a function to save a paper completely (with its chunks)
        pass
