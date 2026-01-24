from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.api.dependencies import get_current_user, get_db
from backend.schemas.category import Category
from backend.schemas.domain import Domain
from backend.services.domain_service import DomainService

router = APIRouter(prefix="/domains", tags=["domains"])


@router.get("/", response_model=List[Domain])
async def get_domains(
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    domains = DomainService.get_all_domains(session)
    if not domains:
        return []

    return domains


@router.get("/{domain_id}", response_model=Domain)
async def get_domain(
    domain_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    domain = DomainService.get_domain_by_id(session, domain_id)

    if not domain:
        raise HTTPException(
            status_code=404, detail=f"Domain with ID {domain_id} not found"
        )

    return domain


@router.get("/{domain_id}/categories", response_model=List[Category])
async def get_domain_categories(
    domain_id: int,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    categories = DomainService.get_categories_by_domain_id(session, domain_id)
    if not categories:
        return []

    return categories
