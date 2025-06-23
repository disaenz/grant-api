from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services.grant_service import get_all_grants
from database import get_db
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/grants", tags=["Grants"])

@router.get("/")
async def read_grants(db: AsyncSession = Depends(get_db)):
    logger.debug("Received request for /api/grants")
    try:
        grants = await get_all_grants(db)
        return {"grants": grants}
    except Exception as e:
        logger.error(f"Error fetching grants: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")