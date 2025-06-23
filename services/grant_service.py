from repositories.grant_repository import fetch_all_grants
from mappers import map_grants_response

async def get_all_grants(db):
    grants = await fetch_all_grants(db)
    return map_grants_response(grants)