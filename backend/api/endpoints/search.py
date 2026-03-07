from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.search import ChunkResult, SearchQuery, SearchResult
from backend.services import SearchService

router = APIRouter(prefix="/search", tags=["search"])


@router.post("/", response_model=List[SearchResult])
async def search_papers(
    search_query: SearchQuery,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        results = SearchService.search_papers(
            session,
            search_query.query,
            top_k_papers=search_query.top_k_papers,
            top_k_chunks=search_query.top_k_chunks,
            chunk_relevance_threshold=search_query.chunk_relevance_threshold,
        )

        search_results = []
        for paper_ranked in results:
            chunks = []
            if paper_ranked.chunks:
                chunks = [
                    ChunkResult(chunk=c.chunk, score=c.score)
                    for c in paper_ranked.chunks
                ]

            search_result = SearchResult(
                paper=paper_ranked.paper,
                score=paper_ranked.score,
                chunks=chunks,
            )
            search_results.append(search_result)

        return search_results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
