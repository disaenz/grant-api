from utils import format_date
from schemas.grant import GrantCreate, GrantUpdate
from typing import Any, Dict, List
from models.grant import Grant as GrantModel
from datetime import datetime


def map_grant_response(grant: GrantModel) -> Dict[str, Any]:
    if not isinstance(grant, GrantModel):
        raise TypeError(f"map_grant_response expected GrantModel, got {type(grant)}")

    return {
        "id": grant.id,
        "name": grant.name,
        "program": grant.program,
        "type": grant.grant_type,
        "status": grant.status,
        "startDate": format_date(grant.start_date),
        "deadline": format_date(grant.deadline),
        "budgetRange": grant.budget_range,
        "createdAt": grant.created_at.isoformat() if grant.created_at else None,
        "updatedAt": grant.updated_at.isoformat() if grant.updated_at else None,
        "notes": grant.notes,
    }

def map_grants_response(grants: List[GrantModel]) -> List[Dict[str, Any]]:
    return [map_grant_response(g) for g in grants]

def map_create_to_model(grant_in: GrantCreate) -> dict:
    
    fmt = "%m-%d-%Y"

    return {
        "name": grant_in.name,
        "program": grant_in.program,
        "grant_type": grant_in.type,
        "status": grant_in.status,
        "start_date": datetime.strptime(grant_in.startDate, fmt).date(),
        "deadline": datetime.strptime(grant_in.deadline, fmt).date(),
        "budget_range": grant_in.budgetRange,
        "notes": grant_in.notes,
    }

def map_update_to_model(grant_id: int, grant_in: GrantUpdate) -> dict:
    
    fmt = "%m-%d-%Y"

    return {
        "id": grant_id,
        "name": grant_in.name,
        "program": grant_in.program,
        "grant_type": grant_in.type,
        "status": grant_in.status,
        "start_date": datetime.strptime(grant_in.startDate, fmt).date(),
        "deadline": datetime.strptime(grant_in.deadline, fmt).date(),
        "budget_range": grant_in.budgetRange,
        "notes": grant_in.notes,
    }