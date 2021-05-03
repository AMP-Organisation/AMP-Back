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


@medicine_router.patch("/")
def get_all_medicine(body_medicine: medicine_schema.medicinePatch, dbSession: Session = Depends(db_dependencies.get_db)):
    print("dans PATCH medicine")
    print(body_medicine)
    med = crudMed.patch_medicine(body_medicine, dbSession, body_medicine.id)
    return med


@medicine_router.delete("/")
def get_all_medicine(body_medicine: medicine_schema.medicinePatch, dbSession: Session = Depends(db_dependencies.get_db)):
    print("le body")
    print(body_medicine)
    print(body_medicine.id)
    elem_deleted = crudMed.delete_medicine(dbSession, body_medicine.id)
    #elem_deleted = crudBaseOBJMedicine.remove(dbSession, model_id=body_medicine.id)
    return elem_deleted

# cette fonction retourne une liste de string corespondant au type de medoc existant
@medicine_router.get("/type/{id_med}")
def get_all_type_medicine(id_med: int, dbSession: Session = Depends(db_dependencies.get_db)):
    print("In GET type according to ID")
    print(id_med)
    list_type = "toto"
    list_type = crudMed.join_get_type_of_a_medicine(dbSession, id_med)
    #return [ {'id':'toto'}, {'id':'titi'}, {'id':'tyty'}]
    return list_type
