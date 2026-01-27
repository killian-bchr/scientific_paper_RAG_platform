from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.chunk import Chunk
from backend.services.chunk_service import ChunkService

router = APIRouter(prefix="/chunks", tags=["chunks"])


@router.get("/", response_model=List[Chunk])
async def get_chunks(
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    chunks = ChunkService.get_all_chunks(session)
    if not chunks:
        return []

    return chunks


@router.get("/{chunk_id}", response_model=Chunk)
async def get_chunk(
    chunk_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    chunk = ChunkService.get_chunk_by_id(session, chunk_id)
    if not chunk:
        raise HTTPException(
            status_code=404, detail=f"Chunk with ID {chunk_id} not found"
        )

    return chunk
