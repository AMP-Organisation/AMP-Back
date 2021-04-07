from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.db_dependencies import get_db
from ..database.models.symtoms_model import Symptoms
from ..schemas import symptoms_schema, disease_schemas
from ..crud.crud_symptoms import symptoms

symptoms_router = APIRouter(
    prefix='/symptoms'
)


@symptoms_router.get('/getAll', response_model=List[symptoms_schema.SymptomsResponse])
def all_symptoms(*, db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> List[Symptoms]:
    return symptoms.get_multi(db, skip=skip, limit=limit)


# user search for disease with those symptoms
@symptoms_router.post('/getSymptoms', response_model=List[disease_schemas.responseDisease])
def disease_filtered_by_symptoms(*, db: Session = Depends(get_db), symptoms_in: symptoms_schema.GetSymptoms):
    all_disease_filtered = symptoms.get_disease_filtered(db, symptoms_in.all_name)

    if not all_disease_filtered:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="We are sorry but, no disease correspond to your symptoms...",
        )

    return all_disease_filtered
