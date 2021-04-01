from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import session, base_class
from ..crud import disease_crud, crud_base
from ..core import db_dependencies
from ..schemas import disease_schemas
from ..database.models import disease_model

diseases_router = APIRouter(
    prefix="/diseases",
    tags=["diseases"],
)

crudObjDisease = disease_crud.CRUD_disease()
crudBaseOBJ = crud_base.CRUDBase([disease_model.disease, disease_model.disease, disease_model.disease_base])

# route to get all the disease 
# rajouter : response_model=user_schema.UserResponse)
@diseases_router.get("/")
def get_all_disease(db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    print("Query to get all the disease")
    all_disease = crudObjDisease.get_all_disease(db, limit)
    return all_disease


@diseases_router.get("/type")
def get_all_disease(id: int = -1, db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    print("Query for the type")
    all_disease_type = crudObjDisease.get_all_disease_type(db, limit)
    return all_disease_type
    
@diseases_router.get("/{id_dis}")
def get_all_disease(id_dis: int, db: Session = Depends(db_dependencies.get_db)):
    print("Query to get one the disease")
    one_disease = crudObjDisease.get_one_disease(db, id_dis)
    print("le resultat obtenu")
    print(one_disease)
    return one_disease

# note : je dirais que seul les admin pourrait en rajouter non ?
@diseases_router.post("/")
def add_a_disease(body_disease: disease_schemas.moreDisease, dbSession: Session = Depends(db_dependencies.get_db)):
    print("data received in body")
    print(body_disease)
    #new_disease_added = crudBaseOBJ.create(dbSession, obj_in=body_disease)
    new_disease_added = crudObjDisease.add_a_disease(dbSession, body_disease)
    return new_disease_added


# rappel : 
# put -> modification compplpete
# patch -> modification partielle
@diseases_router.put("/")
def put_disease(body_disease: disease_schemas.moreDisease, dbSession: Session = Depends(db_dependencies.get_db)):
    print("*in PUT route for disease*")
    print(body_disease)
    updated_disease = crudObjDisease.update_disease(dbSession, body_disease)
    return updated_disease
    #return {"message":"in progress PUT"}

# for now, PATCH only work on descriptioon and name
# And PARTIALLY : the ID stay the same, juste up the others data
@diseases_router.patch("/")
def patch_disease(body_disease: disease_schemas.diseasePatch, dbSession: Session = Depends(db_dependencies.get_db)):
    print("*in PATCH route for disease*")
    print(body_disease)
    patched = crudObjDisease.patch_a_disease(dbSession, body_disease, body_disease.id)
    return patched

# on va vraiment faire un delete ? en tout cas seul les admins devrait pouvoir le faire non ?
@diseases_router.delete("/")
def delete_a_disease(body_disease: disease_schemas.disease, dbSession: Session = Depends(db_dependencies.get_db)):
    print("Delete of a disease")
    print(body_disease)
    print(body_disease.id)
    elem_to_del = crudObjDisease.delete_disease(dbSession, body_disease.id)
    return elem_to_del
    #return body_disease.id