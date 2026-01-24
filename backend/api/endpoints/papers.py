from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.chunk import Chunk
from backend.schemas.paper import Paper
from backend.services.paper_service import PaperService

router = APIRouter(prefix="/papers", tags=["papers"])


@router.get("/", response_model=List[Paper])
async def get_papers(
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    papers = PaperService.get_all_papers(session)
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
