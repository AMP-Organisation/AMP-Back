# created by BBR on 10-05-21
from sqlalchemy.orm import Session 
from typing import List
from fastapi.encoders import jsonable_encoder
from ..crud.crud_base import CRUDBase
from ..schemas.followup_schema import followup_imc

from ..database.models import followup_model

# étant donné que pourrait avoir plusieurs suivi, est ce qu'on fait un ensemble 
# (crud, schema et mode) pour chaque type de suivi ou un ensemble qui prend tout
class CRUD_IMC:
    # je limite a 365 car il pourrait y en avoir beaucoup (et une année c'est assez par defaut)
    def get_all_data(self, dbSession: Session, limit: int):
        return dbSession.query(followup_model.imc_suivi).limit(limit).all()


    def get_one_item(self, dbSession: Session, id_to_find: int):
        return dbSession.query(followup_model.imc_suivi).filter(followup_model.imc_suivi.id == id_to_find)


    def add_one_elem(self, body_followup_imc: followup_imc, dbSession: Session):
        if Session == None:
            return 'Null'
        newData = followup_model.imc_suivi()
        newData.user_id = body_followup_imc.id_user
        newData.imc_computed = body_followup_imc.imc
        newData.weight = body_followup_imc.weight
        newData.date = body_followup_imc.date

        dbSession.add(newData)
        dbSession.commit()
        dbSession.refresh(newData)
        return newData


