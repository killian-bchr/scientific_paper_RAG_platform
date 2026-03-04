from typing import Dict

from sqlalchemy.orm import Session

from backend.database.repositories import (
    AuthorRepository,
    CategoryRepository,
    DomainRepository,
    PaperRepository,
)


class StatsService:
    @staticmethod
    def compute_stats(session: Session) -> Dict[str, int]:
        return {
            "total_papers": PaperRepository.count_papers(session),
            "total_authors": AuthorRepository.count_authors(session),
            "total_domains": DomainRepository.count_domains(session),
            "total_categories": CategoryRepository.count_categories(session),
        }
