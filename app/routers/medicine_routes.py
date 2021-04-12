from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import session, base_class
from ..crud import disease_crud, crud_base
from ..core import db_dependencies
from ..schemas import disease_schemas
from ..database.models import disease_model

medicine_router = APIRouter(
    prefix="/medicines",
    tags=["medicines"],
)

crudBaseOBJ = crud_base.CRUDBase([disease_model.disease, disease_model.disease, disease_model.disease_base])

@medicine_router.get("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress GET medicine"}

@medicine_router.post("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress POST medicine"}

@medicine_router.patch("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress PATCH medicine"}

@medicine_router.delete("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress DELETE medicine"}