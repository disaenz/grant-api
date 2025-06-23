from sqlalchemy.future import select
from models.grant import Grant
from models.calendar import Calendar

async def fetch_grants_by_year(db, year: int):
    result = await db.execute(
        select(Grant).join(Calendar).filter(Calendar.year == year)
    )
    return result.scalars().all()
