from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import session, base_class
from ..crud import crud_base, crud_medicine
from ..core import db_dependencies
from ..schemas import medicine_schema
from ..database.models import medicine_model

medicine_router = APIRouter(
    prefix="/medicines",
    tags=["medicines"],
)

crudBaseOBJMedicine = crud_base.CRUDBase([medicine_model.medicine])
crudMed = crud_medicine.CRUD_medicine()


@medicine_router.get("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    #allMedi = crudBaseOBJMedicine.get_multi(db)
    allMedi = crudMed.get_all_medicine(db)
    print("all medicine")
    print(allMedi)
    return allMedi


@medicine_router.get("/{id_med}")
def get_one_medicine(id_med: int, db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    one_med = crudMed.get_one_med(id_med, db)
    print("one medicine")
    print(one_med)
    return one_med


@medicine_router.post("/")
def add_a_medicine(body_medicine: medicine_schema.medicine, dbSession: Session = Depends(db_dependencies.get_db)):
    
    return { "message": "in progress POST medicine"}

@medicine_router.patch("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress PATCH medicine"}

@medicine_router.delete("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress DELETE medicine"}