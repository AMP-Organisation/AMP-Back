# created by BBR on 13-04-21
from sqlalchemy.orm import Session 
from typing import List
from fastapi.encoders import jsonable_encoder
from ..crud.crud_base import CRUDBase

from ..database.models.active_ingredient_model import Active_Ingredient
from ..schemas.medicine_schema import CreatePrincipleActive, UpdatePrincipleActive

from ..database.models import medicine_model

class CRUD_medicine:
    # I set a limit to 100 by default
    def get_all_medicine(self, dbSession: Session, limit: int = 100):
        return dbSession.query(medicine_model.medicine).limit(limit).all()

    def get_all_thumbnail(self, dbSession: Session, limit: int = 100):
        return dbSession.query(medicine_model.thumbnail).limit(limit).all()

    def get_one_thumbnail(self, dbSession: Session, id_med: int):
        return dbSession.query(medicine_model.thumbnail).filter(medicine_model.thumbnail.id == id_med).first()

    def get_one_med(self, id_med: int, dbSession: Session):
        resp = dbSession.query(medicine_model.medicine).filter(medicine_model.medicine.id == id_med).first()
        return resp

    def add_one_med(self, new_medicine: medicine_model.medecineShort, dbSession: Session):
        med_to_add = medicine_model.medicine()
        med_to_add.name = new_medicine.name
        med_to_add.description = new_medicine.description
        med_to_add.dose = new_medicine.dose
        med_to_add.dose_max = new_medicine.dose_max
        med_to_add.list_type = new_medicine.list_type
        med_to_add.delay = new_medicine.delay
        dbSession.add(med_to_add)
        dbSession.commit()
        dbSession.refresh(med_to_add)
        return new_medicine
    
    def patch_medicine(self, medicine_body: medicine_model.medicine, dbSession: Session, id_med: int):
        med_to_update = dbSession.query(medicine_model.medicine).filter(medicine_model.medicine.id == id_med).first()

        med_to_update.name = medicine_body.name if medicine_body.name != None else med_to_update.name
        med_to_update.description = medicine_body.description if medicine_body.description != None else med_to_update.description
        med_to_update.dose = medicine_body.dose if medicine_body.dose != None else med_to_update.dose
        med_to_update.dose_max = medicine_body.dose_max if medicine_body.dose_max != None else med_to_update.dose_max
        med_to_update.delay = medicine_body.delay if medicine_body.delay != None else med_to_update.delay

        dbSession.commit()
        patched = dbSession.query(medicine_model.medicine).filter(medicine_model.medicine.id == id_med).first()
        return patched

    def delete_medicine(self, dbSession: Session, id_med: int):
        elem_to_del = dbSession.query(medicine_model.medicine).filter(medicine_model.medicine.id == id_med).first()
        dbSession.delete(elem_to_del)
        dbSession.commit()
        return elem_to_del

    def join_get_type_of_a_medicine(self, dbSession: Session, id_med: int):
        resp = dbSession.query(medicine_model.medicine).get(id_med)

        type_list = [dbSession.query(medicine_model.medecine_type).get(current_id) for current_id in resp.list_type]
        
        return type_list
        
class CRUDMedicine(CRUDBase[Active_Ingredient, CreatePrincipleActive, UpdatePrincipleActive]):

    def get_all_principle_active(self, db: Session, all_id: List[int]) -> List[Active_Ingredient]:
        all_active_ingredient = [db.query(self.model).get(current_id) for current_id in all_id]
        return all_active_ingredient
    pass
  
 
medicine = CRUDMedicine(Active_Ingredient)
