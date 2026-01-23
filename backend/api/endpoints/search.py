from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.search import SearchQuery, SearchResult
from backend.services.search_service import SearchService

router = APIRouter()


@router.post("/search", response_model=List[SearchResult])
async def search_papers(
    search_query: SearchQuery,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        raw_results = SearchService.search_papers(
            session,
            search_query.query,
            k=search_query.limit,
        )

        search_results = [
            SearchResult(paper=paper, score=float(score))
            for paper, score in raw_results
        ]

        return search_results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
