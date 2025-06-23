from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.grant_service import get_all_grants_by_year
from database import get_db
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/grants", tags=["Grants"])

@router.get("/")
async def read_grants(year: int, db: AsyncSession = Depends(get_db)):
    logger.debug(f"Received request for /grants for year: {year}")
    grants = await get_all_grants_by_year(db, year)
    return {"grants": grants}
