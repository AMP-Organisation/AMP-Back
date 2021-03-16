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

crudObj = disease_crud.CRUD_disease()
crudBaseOBJ = crud_base.CRUDBase([disease_model.disease, disease_model.disease, disease_model.disease_base])

# route to get all the disease 
# rajouter : response_model=user_schema.UserResponse)
@diseases_router.get("/")
def get_all_disease(id: int = -1, db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    print("on va faire la query")
    print("")
    all_disease = crudObj.get_all_disease(db, limit)
    return all_disease

@diseases_router.get("/type")
def get_all_disease(id: int = -1, db: Session = Depends(db_dependencies.get_db), limit: int = 10):
    print("on va faire la query ppour les type")
    all_disease_type = crudObj.get_all_disease_type(db, limit)
    return all_disease_type

# note : je dirais que seul les admin pourrait en rajouter non ?
@diseases_router.post("/")
def add_a_disease(body_disease: disease_schemas.baseDisease, dbSession: Session = Depends(db_dependencies.get_db)):
    print("le body")
    print(body_disease)
    #new_disease_added = crudBaseOBJ.create(dbSession, obj_in=body_disease)
    new_disease_added = crudObj.add_a_disease(db, body_disease)
    return new_disease_added


# rappel : 
# put -> modification compplpete
# patch -> modification partielle
@diseases_router.put("/")
def put_disease(body_disease: disease_schemas.baseDisease, dbSession: Session = Depends(db_dependencies.get_db)):

    return {"message":"in progress PUT"}


@diseases_router.patch("/")
def patch_disease(body_disease: disease_schemas.baseDisease, dbSession: Session = Depends(db_dependencies.get_db)):
    
    return {"message":"in pprogress PATCH"}


# on va vraiment faire un delete ? en tout cas seul les admins devrait pouvoir le faire non ?
@diseases_router.delete("/")
def delete_a_disease(body_disease: disease_schemas.disease, dbSession: Session = Depends(db_dependencies.get_db)):
    print("la supppression d'une maladie de la bdd")
    print(body_disease)
    print(body_disease.id)
    elem_to_del = crudObj.delete_disease(dbSession, body_disease.id)
    return elem_to_del