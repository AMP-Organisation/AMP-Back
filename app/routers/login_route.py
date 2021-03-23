from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..crud import user_crud
from ..schemas import user_schema, message, group_schema

login_router = APIRouter(
    prefix='/login'
)


@login_router.get('', response_model=message.Message)
def connection_user():
    return {"message": "You have to use a POST request"}


"""
# user log in
@router.post('/', response_model=user_schema.UserResponse)
def connection_user():
    return {"message":"in progress"}
"""


# new user
@login_router.post('/signup', response_model=user_schema.UserResponse)
def sign_up_user(body: user_schema.UserBase):
    return {"message": "in progress"}
