from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder


from ..database.models import medicine_model


class CRUD_medicine:
    # I set a limit to 100 by default
    def get_all_medicine(self, dbSession: Session, limit: int = 100):
        return dbSession.query(medicine_model.medicine).limit(limit).all()

    def get_one_med(self, id_med: int, dbSession: Session):
        resp = dbSession.query(medicine_model.medicine).filter(medicine_model.medicine.id == id_med).first()
        return resp
