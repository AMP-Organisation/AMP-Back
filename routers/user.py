from fastapi import APIRouter, Depends
from services import user_service
from schemas import schemas
from sqlalchemy.orm import Session
from Database import database

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

get_db = database.get_db


@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user_service.show(id, db)
