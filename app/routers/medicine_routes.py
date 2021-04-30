from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import session, base_class
from ..crud import crud_base, crud_medicine
from ..core import db_dependencies
from ..schemas import medicine_schema
from ..database.models import medicine_model

medicine_router_bis = APIRouter(
    prefix="/medicines",
    tags=["medicines"],
)

crudBaseOBJMedicine = crud_base.CRUDBase([medicine_model.medicine])
crudMed = crud_medicine.CRUD_medicine()


@medicine_router_bis.get("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    #allMedi = crudBaseOBJMedicine.get_multi(db)
    allMedi = crudMed.get_all_medicine(db)
    return allMedi

@medicine_router_bis.get("/thumbnail/{id_thumb}")
def get_all_thumbnail(id_thumb: int, db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    oneThumbnail = crudMed.get_one_thumbnail(db, id_thumb)
    return oneThumbnail

@medicine_router_bis.get("/thumbnail")
def get_all_thumbnail(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    allThumbnail = crudMed.get_all_thumbnail(db)
    return allThumbnail


@medicine_router_bis.get("/{id_med}")
def get_one_medicine(id_med: int, db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    one_med = crudMed.get_one_med(id_med, db)
    return one_med


@medicine_router_bis.post("/")
def add_a_medicine(body_medicine: medicine_schema.medicinePost, dbSession: Session = Depends(db_dependencies.get_db)):
    print("dans POST medicine")
    print(body_medicine)
    new_med_created = crudMed.add_one_med(body_medicine, dbSession)
    return new_med_created

# TODO: path
@medicine_router_bis.patch("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress PATCH medicine"}

# TODO: delete
@medicine_router_bis.delete("/")
def get_all_medicine(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    return { "message": "in progress DELETE medicine"}