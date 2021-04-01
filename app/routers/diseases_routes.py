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

# In this function I call the put function to update totally and no partially
@diseases_router.patch("/")
def patch_disease(body_disease: disease_schemas.diseasePatch, dbSession: Session = Depends(db_dependencies.get_db)):
    print("*in PATCH route for disease*")
    print(body_disease)
    disease_in_base = crudObjDisease.get_one_disease(dbSession, body_disease.id)
    print("disease to Patch")
    print(disease_in_base)
    print(disease_in_base.id)
    print(disease_in_base.is_treatment)
    print(disease_in_base.danger_level)
    newName = body_disease.name if body_disease.name != None else disease_in_base.name_disease
    newDescription = body_disease.description if body_disease.description != None else disease_in_base.description
    # i create a full schema object from the data receive (to update) and data in db
    updated_disease = disease_schemas.moreDisease(
        id = disease_in_base.id,
        name = newName,
        description = newDescription,
        is_vaccine = disease_in_base.is_vaccine,
        is_treatment = disease_in_base.is_treatment,
        danger_level = disease_in_base.danger_level
    )
    print(updated_disease)
    updated_disease_final = crudObjDisease.update_disease(dbSession, updated_disease)
    return updated_disease_final
    #return {"message":"in progress PATCH"}


# on va vraiment faire un delete ? en tout cas seul les admins devrait pouvoir le faire non ?
@diseases_router.delete("/")
def delete_a_disease(body_disease: disease_schemas.disease, dbSession: Session = Depends(db_dependencies.get_db)):
    print("Delete of a disease")
    print(body_disease)
    print(body_disease.id)
    elem_to_del = crudObjDisease.delete_disease(dbSession, body_disease.id)
    return elem_to_del
    #return body_disease.id