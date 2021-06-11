from typing import Optional, List
from pydantic import BaseModel
import datetime


class PillboxBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    beginning_date: Optional[datetime.datetime]
    ending_date: Optional[datetime.datetime]
    list_treatment: Optional[List[int]]
    user_id: Optional[str]


class CreatePillbox(PillboxBase):
    name: str
    description: str
    list_treatment: List[int]
    beginning_date: datetime.datetime


class UpdatePillbox(PillboxBase):
    id: int
    name: Optional[str]
    description: Optional[str]
    beginning_date: Optional[datetime.datetime]
    ending_date: Optional[datetime.datetime]
    list_treatment: Optional[int]
    user_id: Optional[str]


class GetUserPillbox(BaseModel):
    id: int


class PillboxResponse(PillboxBase):
    class Config:
        orm_mode = True
