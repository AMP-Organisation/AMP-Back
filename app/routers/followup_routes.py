from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import session, base_class

from ..crud import crud_base, crud_imc

from ..core import db_dependencies
from ..schemas import followup_schema
from ..database.models import followup_model


follow_up_router = APIRouter(
    prefix="/followup",
    tags=["/followup"]
)

crud_obj_imc = crud_imc.CRUD_IMC()

# attention la j'ai précisé /imc ce qui donne comme route /followup/imc
# comme ca on pourra avoir d'autre route followup/toto 
@follow_up_router.get("/imc")
def get_all_data(db_session: Session = Depends(db_dependencies.get_db), limit: int = 365, id: int = 0):
    print("GET ")
    all_data = crud_obj_imc.get_all_data(db_session, limit)
    return "in progress"

@follow_up_router.post("/imc")
def add_new_imc_data(body_followup_imc: followup_schema.followup_imc, \
        db_session: Session = Depends(db_dependencies.get_db), ):
    print("POST new imc")
    print(body_followup_imc)
    new_elem = None
    dbSession = db_session
    new_elem = crud_obj_imc.add_one_elem(body_followup_imc, dbSession)
    return new_elem
