from typing import List, Optional

from sqlalchemy.orm import Session, joinedload

from backend.database.tables import DomainORM


class DomainRepository:
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
    def get_existing_domain(session: Session, domain: str) -> Optional[DomainORM]:
        return session.query(DomainORM).filter_by(name=domain).first()

    @staticmethod
    def count_domains(session: Session) -> int:
        return session.query(DomainORM).count()
