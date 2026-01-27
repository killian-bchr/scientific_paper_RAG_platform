from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.stats import Stats
from backend.services.stats_service import StatsService

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/", response_model=Stats)
def get_stats(
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    stats = StatsService.compute_stats(session)
    return Stats(**stats)
