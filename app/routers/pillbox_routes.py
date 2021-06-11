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


@pillbox_router.put('/updatePillbox', response_model=message.Message)
def update_pillbox(*, db: Session = Depends(get_db), pillbox_in: pillbox_schema.UpdatePillbox):
    pillbox_found = pillbox.get(db=db, model_id=pillbox_in.id)
    pillbox.addTreatment(db=db, updated_pillbox=pillbox_in, ori_pillbox=pillbox_found)

    return {"message": "Pillulier mis à jour"}


@pillbox_router.post('/createPillbox', response_model=message.Message)
def create_pillbox(*, db: Session = Depends(get_db), pillbox_in: pillbox_schema.CreatePillbox):
    new_pillbox = pillbox.verifyPillbox(db=db, pillbox_in=pillbox_in)
    if new_pillbox:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ce pillulier existe déjà dans le système",
        )
    pillbox.create(db=db, obj_in=pillbox_in)
    return {"message": "Pillulier créé"}


@pillbox_router.delete('/deletePillbox', response_model=message.Message)
def create_pillbox(*, db: Session = Depends(get_db), pillbox_in: pillbox_schema.GetUserPillbox):
    print(pillbox_in)
    pillbox.remove(db=db, model_id=pillbox_in.id)
    return {"message": "Pillulier supprimer"}
