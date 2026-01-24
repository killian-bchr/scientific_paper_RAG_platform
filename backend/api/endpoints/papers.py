from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.chunk import Chunk
from backend.schemas.paper import Paper
from backend.services.paper_service import PaperService

router = APIRouter(prefix="/papers", tags=["papers"])


@router.get("/", response_model=List[Paper])
async def get_papers(
    domain_id: Optional[int] = None,
    category_id: Optional[int] = None,
    start_year: Optional[int] = None,
    end_year: Optional[int] = None,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    papers = PaperService.get_filtered_papers(
        session=session,
        domain_id=domain_id,
        category_id=category_id,
        start_year=start_year,
        end_year=end_year,
    )
    if not papers:
        return []

    return papers


@router.get("/{paper_id}", response_model=Paper)
async def get_paper(
    paper_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    paper = PaperService.get_paper_by_id(session, paper_id)
    if not paper:
        raise HTTPException(
            status_code=404, detail=f"Paper with ID {paper_id} not found"
        )

    return paper


@router.get("/{paper_id}/chunks", response_model=List[Chunk])
async def get_paper_chunks(
    paper_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    chunks = PaperService.get_chunks_by_paper_id(session, paper_id)
    if not chunks:
        return []

    return chunks
