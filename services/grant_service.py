from sqlalchemy.exc import NoResultFound
from repositories.grant_repository import get_grant, list_grants, create_grant, update_grant
from schemas.grant import GrantCreate
from mappers import map_grant_response, map_grants_response, map_create_to_model, map_update_to_model

async def fetch_grant(db, grant_id: int):
    try:
        grant = await get_grant(db, grant_id)
    except NoResultFound:
        return None
    return map_grant_response(grant)

async def fetch_all(db):
    grants = await list_grants(db)
    return map_grants_response(grants)

async def add_grant(db, grant_in: GrantCreate):
    repo_model = map_create_to_model(grant_in)
    grant = await create_grant(db, grant_in=repo_model)
    return grant.id

async def change_grant(db, grant_id: int, grant_in):
    repo_model = map_update_to_model(grant_id, grant_in)
    grant = await update_grant(db, grant_id, updates=repo_model)
    return grant.id