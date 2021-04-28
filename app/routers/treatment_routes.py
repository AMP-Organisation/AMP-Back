from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db_dependencies import get_db
from ..crud.treatment_crud import treatment
from ..schemas import treatment_schema, medicine_schema, message

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


@treatment_router.post('/updateTreatment', response_model=message.Message)
def show_treatment_related(*, db: Session = Depends(get_db), treatment_in: treatment_schema.TreatmentBase):
    current_treatment = treatment.get(db=db, model_id=treatment_in.id)

    if not current_treatment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The treatment do not exist in the system.",
        )

    treatment.update(db=db, db_obj=current_treatment, obj_in=treatment_in)
    return {"message": "Traitement mis à jour"}


@treatment_router.get('/treatmentUser/{user_id}', response_model=List[treatment_schema.TreatmentResponse])
def show_treatment_related(user_id: int, db: Session = Depends(get_db)):
    user_treatment = treatment.user_treatment(db, user_id)
    return user_treatment


@treatment_router.post('/medicineRelated', response_model=List[medicine_schema.medicineResponse])
def show_medicine_related(*, db: Session = Depends(get_db), pillbox_in: treatment_schema.GetTreatment):
    all_medicine_related = treatment.related_medicine(db, pillbox_in.current_treatment)
    return all_medicine_related
