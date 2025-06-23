from sqlalchemy.future import select
from models.grant import Grant

async def fetch_all_grants(db):
    result = await db.execute(select(Grant))
    return result.scalars().all()