import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: Optional[int]
    last_name: str
    first_name: str
    email: str
    username: str
    age: int


class CreateUser(UserBase):
    age: int
    birth_date: datetime.datetime
    dt_inscription: datetime.datetime
    last_login: Optional[datetime.datetime]
    fk_group: int


class UpdateUser(UserBase):
    id: int
    pass


class DeleteUser(BaseModel):
    id: int
    pass


class GetUser(BaseModel):
    username: str
    pass


class UserResponse(UserBase):
    class Config:
        orm_mode = True
