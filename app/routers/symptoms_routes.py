from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.db_dependencies import get_db
from ..schemas import symptoms_schema, disease_schemas
from ..crud.crud_symptoms import symptoms

symptoms_router = APIRouter(
    prefix='/symptoms'
)


# user log in
@symptoms_router.post('/getSymptoms', response_model=List[disease_schemas.responseDisease])
def connection_user(*, db: Session = Depends(get_db), auth_in: symptoms_schema.GetSymptoms):
    all_disease_filtered = symptoms.get_disease_filtered(db, auth_in.all_name)

    if not all_disease_filtered:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="We are sorry but, no disease correspond to your symptoms...",
        )

    return all_disease_filtered
