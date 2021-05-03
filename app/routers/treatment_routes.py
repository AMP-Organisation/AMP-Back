from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..schemas import treatment_schema, medicine_schema
from ..crud.treatment_crud import treatment

treatment_router = APIRouter(
    prefix='/treatment'
)


@treatment_router.get('/', response_model=List[treatment_schema.TreatmentResponse])
def show_relation(*, db: Session = Depends(get_db)):
    pillbox_found = treatment.get_multi(db=db)
    return pillbox_found


@treatment_router.post('/treatmentRelated', response_model=List[treatment_schema.TreatmentResponse])
def show_treatment_related(*, db: Session = Depends(get_db), pillbox_in: treatment_schema.GetTreatments):
    all_treatment_related = treatment.related_treatment(db, pillbox_in.all_treatment)
    return all_treatment_related


@treatment_router.post('/medicineRelated', response_model=List[medicine_schema.medicineResponse])
def show_medicine_related(*, db:Session = Depends(get_db), pillbox_in: treatment_schema.GetTreatment):
    all_medicine_related = treatment.related_medicine(db, pillbox_in.current_treatment)
    return all_medicine_related
