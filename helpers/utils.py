from datetime import date, datetime
from typing import List, Optional, Union

from sqlalchemy.orm import Query, Session, joinedload

from database.tables import (
    AuthorORM,
    CategoryORM,
    ChunkORM,
    DomainORM,
    PaperORM,
    UserORM,
)
from exceptions import InvalidDate


class Utils:
    @staticmethod
    def parse_date(input_date: Union[str, date, datetime]) -> Optional[date]:
        if input_date is None:
            return None

        if isinstance(input_date, date) and not isinstance(input_date, datetime):
            return input_date

        if isinstance(input_date, datetime):
            return input_date.date()

        if isinstance(input_date, str):
            try:
                return datetime.strptime(input_date, "%Y-%m-%d").date()
            except ValueError:
                pass

            try:
                return datetime.strptime(input_date, "%Y-%m").date()
            except ValueError:
                pass

        raise InvalidDate(f"Impossible to parse this date : {input_date}")

    @staticmethod
    def fetch_user_by_username(
        session: Session,
        username: str,
    ) -> Optional[UserORM]:
        return session.query(UserORM).filter_by(username=username).first()

    @staticmethod
    def fetch_all_users(session: Session) -> List[UserORM]:
        return session.query(UserORM).all()

    @staticmethod
    def fetch_all_authors(session: Session) -> List[AuthorORM]:
        return (
            session.query(AuthorORM)
            .options(
                joinedload(AuthorORM.papers),
            )
            .all()
        )

    @staticmethod
    def fetch_all_domains(session: Session) -> List[DomainORM]:
        return (
            session.query(DomainORM)
            .options(
                joinedload(DomainORM.categories),
                joinedload(DomainORM.papers),
            )
            .all()
        )

    @staticmethod
    def fetch_all_categories(session: Session) -> List[CategoryORM]:
        return (
            session.query(CategoryORM)
            .options(
                joinedload(CategoryORM.domain),
                joinedload(CategoryORM.papers),
                joinedload(CategoryORM.domain).joinedload(DomainORM.papers),
            )
            .all()
        )

    @staticmethod
    def papers_base_query(session: Session) -> Query[PaperORM]:
        return session.query(PaperORM).options(
            joinedload(PaperORM.domains),
            joinedload(PaperORM.categories),
            joinedload(PaperORM.authors),
        )

    @staticmethod
    def fetch_all_papers(session: Session) -> List[PaperORM]:
        base_query = Utils.papers_base_query(session)
        return base_query.all()

    @staticmethod
    def fetch_paper_by_id(session: Session, paper_id: int) -> PaperORM:
        base_query = Utils.papers_base_query(session)
        return base_query.filter(PaperORM.id == paper_id).first()

    @staticmethod
    def fetch_paper_by_title(session: Session, title: str) -> PaperORM:
        base_query = Utils.papers_base_query(session)
        return base_query.filter(PaperORM.title == title).one()

    @staticmethod
    def fetch_papers_by_period(
        session: Session,
        start_date: Optional[Union[datetime, date, str]] = None,
        end_date: Optional[Union[datetime, date, str]] = None,
    ) -> List[PaperORM]:
        start_date = Utils.parse_date(start_date)
        end_date = Utils.parse_date(end_date)

        query = Utils.papers_base_query(session)

        if start_date:
            query = query.filter(PaperORM.publication_date >= start_date)

        if end_date:
            query = query.filter(PaperORM.publication_date <= end_date)

        return query.all()

    @staticmethod
    def fetch_all_chunks(session: Session) -> List[ChunkORM]:
        return session.query(ChunkORM).all()

    @staticmethod
    def fetch_chunks_by_paper_id(session: Session, paper_id: int) -> List[ChunkORM]:
        return (
            session.query(ChunkORM)
            .filter(ChunkORM.paper_id == paper_id)
            .order_by(ChunkORM.page_no, ChunkORM.id)
            .all()
        )

    @staticmethod
    def fetch_categories_by_domain_id(
        session: Session, domain_id: int
    ) -> List[CategoryORM]:
        return (
            session.query(CategoryORM).filter(CategoryORM.domain_id == domain_id).all()
        )

    @staticmethod
    def get_existing_author(session: Session, name: str) -> Optional[AuthorORM]:
        return session.query(AuthorORM).filter_by(name=name).first()

    @staticmethod
    def get_existing_domain(session: Session, domain: str) -> Optional[DomainORM]:
        return session.query(DomainORM).filter_by(name=domain).first()

    @staticmethod
    def get_existing_category(
        session: Session, category: str, domain: str
    ) -> Optional[CategoryORM]:
        domain_orm = Utils.get_existing_domain(session, domain)
        if domain_orm is None:
            return None

        return (
            session.query(CategoryORM)
            .filter_by(name=category, domain_id=domain_orm.id)
            .first()
        )

    @staticmethod
    def get_existing_paper(session: Session, paper_id: str) -> Optional[PaperORM]:
        return session.query(PaperORM).filter_by(arxiv_id=paper_id).first()

    @staticmethod
    def count_authors(session: Session) -> int:
        return session.query(AuthorORM).count()

    @staticmethod
    def count_papers(session: Session) -> int:
        return session.query(PaperORM).count()

    @staticmethod
    def count_domains(session: Session) -> int:
        return session.query(DomainORM).count()

    @staticmethod
    def count_categories(session: Session) -> int:
        return session.query(CategoryORM).count()

    @staticmethod
    def count_chunks(session: Session) -> int:
        return session.query(ChunkORM).count()
