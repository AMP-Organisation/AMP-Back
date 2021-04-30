from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..schemas import pillbox_schema, message
from ..crud.pillbox_crud import pillbox

pillbox_router = APIRouter(
    prefix='/pillbox'
)


@pillbox_router.post('/', response_model=List[pillbox_schema.PillboxResponse])
def show_relation(*, db: Session = Depends(get_db), pillbox_in: pillbox_schema.GetUserPillbox):
    pillbox_found = pillbox.getPillboxUser(db=db, idUser=pillbox_in.id)
    return pillbox_found
