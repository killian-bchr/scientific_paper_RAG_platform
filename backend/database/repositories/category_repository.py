from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from backend.database.repositories.domain_repository import DomainRepository
from backend.database.tables import CategoryORM, DomainORM


class CategoryRepository:
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
    def fetch_categories_by_domain_id(
        session: Session, domain_id: int
    ) -> List[CategoryORM]:
        return (
            session.query(CategoryORM).filter(CategoryORM.domain_id == domain_id).all()
        )

    @staticmethod
    def get_existing_category(
        session: Session, category: str, domain: str
    ) -> Optional[CategoryORM]:
        domain_orm = DomainRepository.get_existing_domain(session, domain)
        if domain_orm is None:
            return None

        return (
            session.query(CategoryORM)
            .filter_by(name=category, domain_id=domain_orm.id)
            .first()
        )

    @staticmethod
    def count_categories(session: Session) -> int:
        return session.query(CategoryORM).count()
