import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[int]
    last_name: Optional[str]
    first_name: Optional[str]
    email: Optional[str]
    username: Optional[str]
    age: Optional[int]
    height: Optional[float]


class CreateUser(UserBase):
    age: int
    birth_date: datetime.datetime
    dt_inscription: Optional[datetime.datetime]
    last_login: Optional[datetime.datetime]
    fk_group: Optional[int]


class UpdateUser(UserBase):
    id: int
    pass


class DeleteUser(BaseModel):
    id: int
    pass


class GetUser(BaseModel):
    username: Optional[str]
    email: Optional[str]
    pass


class UserResponse(UserBase):
    class Config:
        orm_mode = True
