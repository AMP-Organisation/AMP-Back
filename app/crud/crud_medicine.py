from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder


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
        print("i am adding a new medicine")
        print(new_medicine)
        # erreur ici ^^
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
        #return "in progress"