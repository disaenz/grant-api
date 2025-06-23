from utils import format_date

def map_grant_response(grant):
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

def map_grants_response(grants):
    return [map_grant_response(grant) for grant in grants]