# created by BBR on 10-05-21
from sqlalchemy.orm import Session 
from sqlalchemy.sql import func, and_
from typing import List
from fastapi.encoders import jsonable_encoder
from ..crud.crud_base import CRUDBase
from ..schemas.followup_schema import followup_imc

from ..database.models import followup_model
from datetime import date, datetime, timedelta

from  pprint import pprint

# étant donné que pourrait avoir plusieurs suivi, est ce qu'on fait un ensemble 
# (crud, schema et mode) pour chaque type de suivi ou un ensemble qui prend tout
class CRUD_IMC:
    # je limite a 365 car il pourrait y en avoir beaucoup (et une année c'est assez par defaut)
    def get_all_data(self, dbSession: Session, limit: int):
        return dbSession.query(followup_model.imc_follow_up).limit(limit).all()

    def get_all_data_from_one_user(self, dbSession: Session, limit: int, id_user: int):
        return dbSession.query(followup_model.imc_follow_up).filter(followup_model.imc_follow_up.user_id == id_user).order_by(followup_model.imc_follow_up.date.desc()).limit(limit).all()

    def get_data_period(self, dbSession: Session, id_user: int, nbDay: int):
        timeD = timedelta(days=nbDay)
        today = date.today() + timedelta(days=1)
        before = date.today() - timeD

        last_period = dbSession.query(followup_model.imc_follow_up).filter(followup_model.imc_follow_up.user_id == id_user).filter(followup_model.imc_follow_up.date.between(before, today)).order_by(followup_model.imc_follow_up.date.desc()).all()

        return last_period


    def get_data_period_bis(self, dbSession: Session, id_user: int, nbDay: int):
        #
        # WIP 
        # I am refactoring
        # 
        # new version
        # today = date.today() + timedelta(days=1)
        befor = date.today() -  timedelta(days=nbDay)
        vingtcinq = datetime(2021, 5, 25)
        vingtcinqBis = datetime(2021, 5, 25, 23, 59)
        today = vingtcinq

        print(today)
        print(today.day)
        print(today.month)
        print(today.year)
        # avg_on_day = dbSession.query(func.avg(followup_model.imc_follow_up.imc_computed), func.avg(followup_model.imc_follow_up.weight))\
        #     .filter(and_(followup_model.imc_follow_up.user_id == id_user, followup_model.imc_follow_up.day == today.day, followup_model.imc_follow_up.month == today.month, followup_model.imc_follow_up.year == today.day))\
        #     .all()
        avg_on_day = dbSession.query(func.avg(followup_model.imc_follow_up.imc_computed), func.avg(followup_model.imc_follow_up.weight)).filter(and_(followup_model.imc_follow_up.user_id == id_user, followup_model.imc_follow_up.year == today.year, followup_model.imc_follow_up.month == today.month, followup_model.imc_follow_up.day == today.day)).all()
        print("moyenne pour le 25 MAI")
        print(avg_on_day)
        pprint(avg_on_day)

        i = 0
        res = []
        while i < nbDay:
            theDate = date.today() - timedelta(days=i+1)
            avg_on_day = dbSession.query(func.avg(followup_model.imc_follow_up.imc_computed), func.avg(followup_model.imc_follow_up.weight)).filter(and_(followup_model.imc_follow_up.user_id == id_user, followup_model.imc_follow_up.year == theDate.year, followup_model.imc_follow_up.month == theDate.month, followup_model.imc_follow_up.day == theDate.day)).all()
            res.append({"date":theDate, "day":theDate.day, "month":theDate.month, "year":theDate.year, "user_id":id_user, "imc_computed":round(avg_on_day[0][0], 2), "weight": round(avg_on_day[0][1], 2)})
            i += 1
        print(res)
        
        # TODO : improvment
        # faire une fonction qui remplace les eventuelle valeur manquante par des moyennes ()

        return res

        # faire de cette maniere
        # period = [dbSession.(query).fileter(for jour in last_week)]
        # return "in preogress bis"


    def get_one_item(self, dbSession: Session, id_to_find: int):
        return dbSession.query(followup_model.imc_follow_up).filter(followup_model.imc_follow_up.id == id_to_find)

    def get_last_imc_data(self, dbSession: Session, id_user: int):
        return dbSession.query(followup_model.imc_follow_up).filter(followup_model.imc_follow_up.user_id == id_user).order_by(followup_model.imc_follow_up.date.desc()).first()

    def add_one_elem(self, body_followup_imc: followup_imc, dbSession: Session):
        if Session == None:
            return 'Null'

        print("dans add one element")
        print(body_followup_imc)
        newData = followup_model.imc_follow_up()
        newData.user_id = body_followup_imc.id_user
        newData.imc_computed = body_followup_imc.imc
        newData.weight = body_followup_imc.weight
        newData.date = body_followup_imc.date
        # problems : some date seem not to be added
        newData.day = body_followup_imc.date.day
        newData.month = body_followup_imc.date.month
        newData.year = body_followup_imc.date.year

        dbSession.add(newData)
        dbSession.commit()
        dbSession.refresh(newData)
        return newData

