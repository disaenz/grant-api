from datetime import datetime
from fastapi import HTTPException, status
from schemas.grant import GrantCreate, GrantUpdate
from schemas.error import APIError
from typing import Optional


DATE_FMT = "%m/%d/%Y"
ALLOWED_STATUSES = {"Closed", "Active", "Pending"}
ALLOWED_TYPES = {"New", "Continuation", "Renewal", "Extended", "Closed"}

def _parse_date(date_str: str, field_name: str, required: bool = False) -> datetime.date:
    try:
        if required and (date_str is None or date_str.strip() == "") :
                api_err = APIError(error=f"{field_name!r} was not provided or is empty")
                raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=api_err.model_dump())
        return datetime.strptime(date_str, DATE_FMT).date()
    except ValueError:
        api_err = APIError(error=f"{field_name!r} must be in {DATE_FMT}, got {date_str!r}")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,detail=api_err.model_dump())


def _validate_grant(*, grant_status: Optional[str], grant_type: Optional[str], startDate: Optional[str], deadline: Optional[str], require_dates: bool):
    # grant_status
    if grant_status is not None and grant_status not in ALLOWED_STATUSES:
        api_err = APIError(error=f"status must be one of {sorted(ALLOWED_STATUSES)}, got {grant_status!r}")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=api_err.model_dump())

    # grant_type
    if grant_type is not None and grant_type not in ALLOWED_TYPES:
        api_err = APIError(error=f"type must be one of {sorted(ALLOWED_TYPES)}, got {grant_type!r}")
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=api_err.model_dump())

    # dates
    _parse_date(startDate, "startDate", required=require_dates)
    _parse_date(deadline,  "deadline",  required=require_dates)


def validate_create(gr: GrantCreate) -> GrantCreate:
    _validate_grant(grant_status=gr.status, grant_type=gr.type, startDate=gr.startDate, deadline=gr.deadline, require_dates=True)
    return gr


def validate_update(gr: GrantUpdate) -> GrantUpdate:
    _validate_grant(grant_status=gr.status, grant_type=gr.type, startDate=gr.startDate, deadline=gr.deadline, require_dates=True)
    return gr
