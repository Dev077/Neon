# backend/src/api/rest/__init__.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"} #health check endpoint