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
def update_treatment(*, db: Session = Depends(get_db), treatment_in: treatment_schema.TreatmentBase):
    current_treatment = treatment.get(db=db, model_id=treatment_in.id)

    if not current_treatment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The treatment do not exist in the system.",
        )

    medicine_in = treatment_in.medicine_id
    update_medicine = False
    for medicine in medicine_in:
        if medicine not in current_treatment.medicine_id:
            update_medicine = True

    if not update_medicine:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ce médicament fait déjà partie de cette liste de traitement.",
        )

    treatment.update(db=db, db_obj=current_treatment, obj_in=treatment_in)
    return {"message": "Traitement mis à jour"}


@treatment_router.post('/createTreatment', response_model=message.Message)
def create_treatment(*, db: Session = Depends(get_db), treatment_in: treatment_schema.TreatmentBase):
    current_treatment = treatment.verify_name(db=db, user_id=treatment_in.user_id, name=treatment_in.name)

    if current_treatment:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Un traitement existe déjà avec ce nom",
        )
    treatment.create(db=db, obj_in=treatment_in)
    return {"message": "Le traitement à bien été créé."}


@treatment_router.get('/treatmentUser/{user_id}', response_model=List[treatment_schema.TreatmentResponse])
def get_user_treatments(user_id: int, db: Session = Depends(get_db)):
    user_treatment = treatment.user_treatment(db, user_id)
    return user_treatment


@treatment_router.post('/medicineRelated', response_model=List[medicine_schema.medicineResponse])
def show_all_medicine_related(*, db: Session = Depends(get_db), treatment_in: treatment_schema.GetTreatment):
    all_medicine_related = treatment.related_medicine(db, treatment_in.current_treatment)
    return all_medicine_related


@treatment_router.post('/deleteMedicine', response_model=message.Message)
def delete_medicine(*, db: Session = Depends(get_db), treatment_in: treatment_schema.DeleteMedicineFromTreatment):
    current_treatment = treatment.get(db=db, model_id=treatment_in.id)

    if not current_treatment:
        if not current_treatment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The treatment do not exist in the system."
            )

    treatment.remove_medicine(db=db, medicine_id=treatment_in.medicine_id, treatment_obj=current_treatment)
    return {"message": "Traitement mis à jour"}
