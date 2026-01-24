from typing import List

from sqlalchemy.orm import Session

from backend.database.repositories import CategoryRepository, DomainRepository
from backend.database.tables import CategoryORM, DomainORM


class DomainService:
    @staticmethod
    def get_all_domains(session: Session) -> List[DomainORM]:
        return DomainRepository.fetch_all_domains(session)

    @staticmethod
    def get_domain_by_id(session: Session, domain_id: int) -> DomainORM:
        return session.query(DomainORM).filter(DomainORM.id == domain_id).first()

    @staticmethod
    def get_categories_by_domain_id(
        session: Session, domain_id: int
    ) -> List[CategoryORM]:
        return CategoryRepository.fetch_categories_by_domain_id(session, domain_id)

    @staticmethod
    def create_domain() -> DomainORM:
        # TODO
        pass
