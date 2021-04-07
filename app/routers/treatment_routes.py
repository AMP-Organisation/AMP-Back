from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..schemas import treatment_schema, message
from ..crud.treatment_crud import treatment

treatment_router = APIRouter(
    prefix='/treatment'
)


@treatment_router.get('/', response_model=List[treatment_schema.TreatmentResponse])
def show_relation(*, db: Session = Depends(get_db)):
    pillbox_found = treatment.get_multi(db=db)
    return pillbox_found

