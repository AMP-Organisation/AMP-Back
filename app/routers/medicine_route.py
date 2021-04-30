from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.db_dependencies import get_db
from ..database.models.active_ingredient_model import Active_Ingredient
from ..schemas import medicine_schema
from ..crud.crud_medicine import medicine

medicine_router = APIRouter(
    prefix='/medicine'
)


@medicine_router.get('/', response_model=List[medicine_schema.PrincipleActiveResponse])
def show_all_user(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    :return: all user in database
    """
    all_medicine = medicine.get_multi(db, skip=skip, limit=limit)
    return all_medicine


@medicine_router.post('/find', response_model=List[medicine_schema.PrincipleActiveResponse])
def show_all_user(*, db: Session = Depends(get_db), medicine_in: medicine_schema.GetPrincipleActive) -> Any:
    """
    :return: all user in database
    """
    principle_active_found = medicine.get_all_principle_active(db, medicine_in.id)
    return principle_active_found
