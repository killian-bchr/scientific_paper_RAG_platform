from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.author import Author
from backend.services.authors_service import AuthorService

router = APIRouter()


@router.get("/authors", response_model=List[Author])
async def get_authors(
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    authors = AuthorService.get_all_authors(session)
    if not authors:
        return []

    return authors


@router.get("/authors/{author_id}", response_model=Author)
async def get_author_by_id(
    author_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    author = AuthorService.get_author_by_id(session, author_id)
    if not author:
        raise HTTPException(
            status_code=404, detail=f"Author with ID {author_id} not found"
        )

    return author
