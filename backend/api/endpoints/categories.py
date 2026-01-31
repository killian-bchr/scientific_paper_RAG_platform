from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.category import Category
from backend.services import CategoryService

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=List[Category])
async def get_categories(
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    categories = CategoryService.get_all_categories(session)
    if not categories:
        return []

    return categories


@router.get("/{category_id}", response_model=Category)
async def get_category(
    category_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    category = CategoryService.get_category_by_id(session, category_id)
    if not category:
        raise HTTPException(
            status_code=404, detail=f"Category with ID {category_id} not found"
        )

    return category
