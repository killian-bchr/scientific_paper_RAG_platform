from backend.core.academic_rankings import (
    A_CONFERENCES,
    A_STAR_CONFERENCES,
    RECOGNIZED_PRESTIGIOUS_JOURNALS,
)
from backend.models import Paper


class ReliabilityScorer:
    @staticmethod
    def score_doi(paper: Paper) -> float:
        return 0.1 if paper.doi else 0.0

    @staticmethod
    def score_citations(paper: Paper) -> float:
        if not paper.cited_by_count:
            return 0.0

        c = paper.cited_by_count

        if c > 200:
            return 0.35
        elif c > 100:
            return 0.3
        elif c > 50:
            return 0.25
        elif c > 20:
            return 0.2
        elif c > 5:
            return 0.17

        return 0.0

    @staticmethod
    def score_fwci(paper: Paper) -> float:
        if not paper.fwci:
            return 0.0

        f = paper.fwci

        if f > 3:
            return 0.35
        elif f > 2:
            return 0.3
        elif f > 1.5:
            return 0.25
        elif f > 1.1:
            return 0.2
        elif f > 0.9:
            return 0.15

        return 0.0

    @staticmethod
    def score_percentile(paper: Paper) -> float:
        if not paper.citation_normalized_percentile:
            return 0.0

        p = paper.citation_normalized_percentile

        if p > 0.95:
            return 0.4
        elif p > 0.9:
            return 0.35
        elif p > 0.8:
            return 0.28
        elif p > 0.6:
            return 0.2
        elif p > 0.4:
            return 0.15

        return 0.0

    @staticmethod
    def contains_venue(journal: str, venues: set[str]) -> bool:
        for venue in venues:
            venue = f" {venue.lower()} "
            if venue in journal:
                return True
        return False

    @staticmethod
    def score_venue(paper: Paper) -> float:
        if not paper.journal:
            return 0.0

        journal = f" {paper.journal.lower()} "

        if ReliabilityScorer.contains_venue(journal, A_STAR_CONFERENCES):
            return 0.9

        if ReliabilityScorer.contains_venue(journal, A_CONFERENCES):
            return 0.7

        if ReliabilityScorer.contains_venue(journal, RECOGNIZED_PRESTIGIOUS_JOURNALS):
            return 0.5

        return 0.3

    @staticmethod
    def compute_reliability_score(paper: Paper) -> float:
        score = 0.0

        score += ReliabilityScorer.score_doi(paper)
        score += ReliabilityScorer.score_venue(paper)
        score += ReliabilityScorer.score_citations(paper)
        score += ReliabilityScorer.score_fwci(paper)
        score += ReliabilityScorer.score_percentile(paper)

        return round(min(score, 1.0), 2)
