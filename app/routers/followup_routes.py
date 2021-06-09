from fastapi import APIRouter, Depends, status, Response
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

@follow_up_router.get("/imc/period")
def get_on_period_data(response: Response, db_session: Session = Depends(db_dependencies.get_db), id_user: int = 0, duration: int = 7):
    if id_user == 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "missing id_user in query"
    on_duration = crud_obj_imc.get_data_period(db_session, id_user, duration)
    return on_duration



# attention la j'ai précisé /imc ce qui donne comme route /followup/imc
# comme ca on pourra avoir d'autre route followup/toto 
@follow_up_router.get("/imc/{id_user}")
def get_all_data(id_user: int, db_session: Session = Depends(db_dependencies.get_db), limit: int = 365):
    all_data = crud_obj_imc.get_all_data_from_one_user(db_session, limit, id_user)
    return all_data


@follow_up_router.get("/imc")
def get_all_data(db_session: Session = Depends(db_dependencies.get_db), limit: int = 365, id: int = 0):
    all_data = crud_obj_imc.get_all_data(db_session, limit)
    return all_data


# j'ai créé des routes lastweek lastmonth et lastyear 
# par simplicité, même si c'est redondant ^^
# sur 7 jour pour une semaine
@follow_up_router.get("/imc/lastweek/{id_user}")
def get_last_week_data(id_user: int, db_session: Session = Depends(db_dependencies.get_db)):
    last_week_data = crud_obj_imc.get_data_period(db_session, id_user, 7)
    return last_week_data


# sur 365 jours
@follow_up_router.get("/imc/lastyear/{id_user}")
def get_last_year_data(id_user: int, db_session: Session = Depends(db_dependencies.get_db)):
    return crud_obj_imc.get_data_period(db_session, id_user, 365)


#sur 31 jour pour un mois
@follow_up_router.get("/imc/lastmonth/{id_user}")
def get_last_month_data(id_user: int, db_session: Session = Depends(db_dependencies.get_db)):
    return crud_obj_imc.get_data_period(db_session, id_user, 31)


@follow_up_router.post("/imc")
def add_new_imc_data(body_followup_imc: followup_schema.followup_imc, \
        db_session: Session = Depends(db_dependencies.get_db), ):
    new_elem = None
    dbSession = db_session
    new_elem = crud_obj_imc.add_one_elem(body_followup_imc, dbSession)
    return new_elem

