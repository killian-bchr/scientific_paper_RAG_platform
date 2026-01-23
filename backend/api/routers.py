from fastapi import APIRouter

from backend.api.endpoints import auth, authors, categories, domains

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(authors.router, prefix="/authors", tags=["authors"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(domains.router, prefix="/domains", tags=["domains"])
