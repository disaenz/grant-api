from pydantic import BaseModel
from typing import Optional
from .error import APIError


class GrantBase(BaseModel):
    name: str
    program: Optional[str] = None
    type: str
    status: str
    startDate: str
    deadline: str
    budgetRange: str
    notes: Optional[str] = None


class GrantCreate(GrantBase):
    pass


class GrantUpdate(BaseModel):
    name: Optional[str] = None
    program: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    startDate: Optional[str] = None
    deadline: Optional[str] = None
    budgetRange: Optional[str] = None
    notes: Optional[str] = None


class GrantResponse(GrantBase):
    id: int
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    class Config:
        orm_mode = True

class GrantCreateResponse(BaseModel):
    success: bool
    id:      int

    class Config:
        orm_mode = True

class GrantUpdateResponse(BaseModel):
    success: bool
    id:      int

    class Config:
        orm_mode = True