from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..crud import crud_auth
from ..auth import security
from ..schemas import auth_schema, message

login_router = APIRouter(
    prefix='/login'
)


@login_router.get('', response_model=message.Message)
def connection_user():
    return {"message": "You have to use a POST request"}


# user log in
@login_router.post('/signin', response_model=auth_schema.AuthResponse)
def connection_user(*, db: Session = Depends(get_db), auth_in: auth_schema.LoginBase):
    user_auth = crud_auth.auth.login(db, auth_in.email, auth_in.password)
    if not user_auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The email or password is incorrect",
        )
    return user_auth


# new user
@login_router.post('/signup', response_model=auth_schema.AuthResponse)
def sign_up_user(*, db: Session = Depends(get_db), auth_in: auth_schema.RegisterBase):
    user_register = crud_auth.auth.register(db, auth_in)
    if not user_register:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Some informations were missing during your registation",
        )
    return user_register
