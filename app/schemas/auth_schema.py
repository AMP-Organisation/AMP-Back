from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AuthBase(BaseModel):
    id: Optional[int]
    last_name: Optional[str]
    first_name: Optional[str]
    email: Optional[str]
    username: Optional[str]
    age: Optional[int]


class LoginBase(AuthBase):
    email: str
    password: str


class RegisterBase(AuthBase):
    email: str
    first_name: str
    last_name: str
    username = str
    password: str
    birth_date: datetime
    fk_group: int
    dt_inscription: Optional[datetime]
    age: int


class AuthResponse(AuthBase):
    class Config:
        orm_mode = True
