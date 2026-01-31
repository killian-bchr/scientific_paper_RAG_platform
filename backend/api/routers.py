from fastapi import APIRouter

from backend.api.endpoints import (
    auth,
    authors,
    categories,
    chunks,
    domains,
    health,
    papers,
    search,
    stats,
    users,
)

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(authors.router)
api_router.include_router(categories.router)
api_router.include_router(chunks.router)
api_router.include_router(domains.router)
api_router.include_router(papers.router)
api_router.include_router(search.router)
api_router.include_router(health.router)
api_router.include_router(stats.router)
api_router.include_router(users.router)
