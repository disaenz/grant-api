from repositories.grant_repository import fetch_grants_by_year
from mappers import map_grants_response

async def get_all_grants_by_year(db, year: int):
    grants = await fetch_grants_by_year(db, year)
    # Map the Grant objects to dictionaries with formatted dates
    return map_grants_response(grants)
