from sqlalchemy.future import select
from sqlalchemy import update as sa_update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from models.grant import Grant

async def get_grant(db: AsyncSession, grant_id: int) -> Grant:
    grant = await db.get(Grant, grant_id)
    if not grant:
        raise NoResultFound(f"Grant {grant_id} not found")
    return grant

async def list_grants(db: AsyncSession) -> list[Grant]:
    result = await db.execute(select(Grant).order_by(Grant.id.asc()))
    return result.scalars().all()

async def create_grant(db: AsyncSession, *, grant_in: dict) -> Grant:
    new = Grant(**grant_in)
    db.add(new)
    await db.commit()
    await db.refresh(new)
    return new

async def update_grant(db: AsyncSession, grant_id: int, *, updates: dict) -> Grant:
    grant = await get_grant(db, grant_id)
    for k, v in updates.items():
        setattr(grant, k, v)
    await db.commit()
    await db.refresh(grant)
    return grant