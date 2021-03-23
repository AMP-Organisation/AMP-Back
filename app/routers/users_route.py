from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..crud import user_crud
from ..schemas import user_schema, message, group_schema

user_router = APIRouter(
    prefix='/users'
)


@user_router.get('/getAll', response_model=List[user_schema.UserResponse])
def show_all_user(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    :return: all user in database
    """
    all_user = user_crud.user.get_multi(db, skip=skip, limit=limit)
    return all_user


@user_router.post('/get', response_model=user_schema.UserResponse)
def show_user(*, db: Session = Depends(get_db), user_in: user_schema.GetUser):
    user_found = user_crud.user.get_by_email(db, user_in.email)
    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user do not exist in the system.",
        )

    return user_found


@user_router.get('/getRelation', response_model=user_schema.UserResponse)
def show_relation(relation: group_schema.GroupBase, db: Session = Depends(get_db)):
    user_found = user_crud.user.relation(db, value=relation.Type)
    return user_found


@user_router.post('/addUser', response_model=user_schema.UserResponse)
def add_user(*, db: Session = Depends(get_db), user_in: user_schema.CreateUser) -> Any:
    user = user_crud.user.get_by_username(db, user_in.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The user already exist in the system with that username : {user_in.username}",
        )
    else:
        new_user = user_crud.user.create(db, obj_in=user_in)
    return new_user


@user_router.put('/updateUser', response_model=user_schema.UserResponse)
def update_user(*, db: Session = Depends(get_db), user_in: user_schema.UpdateUser) -> Any:
    """
    :param db: Database
    :param user_in: The model of the user to update
    :return: the user with his info updated
    """
    user = user_crud.user.get(db, model_id=user_in.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user do not exist in the system.",
        )
    updated_user = user_crud.user.update(db, db_obj=user, obj_in=user_in)
    return updated_user


@user_router.delete('/deleteUser', response_model=message.Message)
def delete_user(*, db: Session = Depends(get_db), user_in: user_schema.DeleteUser) -> Any:
    """
    :param user_in:
    :param db: The current Database
    :return: a message of the user deleted
    """
    user = user_crud.user.get(db, model_id=user_in.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user do not exist in the system.",
        )
    user_crud.user.remove(db, model_id=user.id)
    return {"message": f"User {user.id} with username {user.username} deleted."}
