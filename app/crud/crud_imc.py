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

    # to keep
    # get all data for each day but with several data if there are for a day
    def get_data_period(self, dbSession: Session, id_user: int, nbDay: int):
        timeD = timedelta(days=nbDay)
        today = date.today() + timedelta(days=1)
        before = date.today() - timeD

        last_period = dbSession.query(followup_model.imc_follow_up).filter(followup_model.imc_follow_up.user_id == id_user).filter(followup_model.imc_follow_up.date.between(before, today)).order_by(followup_model.imc_follow_up.date.desc()).all()

        return last_period


    def replaceNoneVal(self, tab):
        oldWeight = None
        oldImc = None
        for i in tab:
            if i['weight'] == None or i['imc_computed']  == None:
                i['weight'] = oldWeight 
                i['imc_computed'] = oldImc
                i['is_fake'] = True
            else:
                oldWeight = i['weight']
                oldImc = i['imc_computed'] 
        return tab

    # get all data for each day but with ONLY ONE for each day : it compute an average
    def get_data_period_average(self, dbSession: Session, id_user: int, nbDay: int):
        befor = date.today() -  timedelta(days=nbDay-1)

        i = 0
        res = []
        while i < nbDay:
            theDate = date.today() - timedelta(days=i+1)
            avg_on_day = dbSession.query(func.avg(followup_model.imc_follow_up.imc_computed), func.avg(followup_model.imc_follow_up.weight)).filter(and_(followup_model.imc_follow_up.user_id == id_user, followup_model.imc_follow_up.year == theDate.year, followup_model.imc_follow_up.month == theDate.month, followup_model.imc_follow_up.day == theDate.day)).all()
            if avg_on_day[0][0] == None:
                res.append({"date":theDate, "day":theDate.day, "month":theDate.month, "year":theDate.year, "user_id":id_user, "imc_computed":None, "weight": None})
            else:
                 res.append({"date":theDate, "day":theDate.day, "month":theDate.month, "year":theDate.year, "user_id":id_user, "imc_computed":round(avg_on_day[0][0], 2), "weight": round(avg_on_day[0][1], 2)})
            i += 1
        
        # TODO : improvment
        # faire une fonction qui remplace les eventuelle valeur manquante par des moyennes ()
        res = self.replaceNoneVal(res)
        return res


    # get all data for each month but with ONLY ONE for each day : it compute an average
    def get_data_period_month_average(self, dbSession: Session, id_user: int, nbMonth: int):
        i = 0
        res = []
        while i < nbMonth:
            theDate = date.today() - timedelta(days=i*30)
            avg_on_month = dbSession.query(func.avg(followup_model.imc_follow_up.imc_computed), func.avg(followup_model.imc_follow_up.weight)).filter(and_(followup_model.imc_follow_up.user_id == id_user, followup_model.imc_follow_up.year == theDate.year, followup_model.imc_follow_up.month == theDate.month)).all()
            if avg_on_month[0][0] == None:
                res.append({"date":theDate, "month":theDate.month, "year":theDate.year, "user_id":id_user, "imc_computed": None, "weight": None})
            else:
                 res.append({"date":theDate, "month":theDate.month, "year":theDate.year, "user_id":id_user, "imc_computed":round(avg_on_month[0][0], 2), "weight": round(avg_on_month[0][1], 2)})
            i += 1

        # faire une fonction pour les mois d'avant ?
        return res


    def get_one_item(self, dbSession: Session, id_to_find: int):
        return dbSession.query(followup_model.imc_follow_up).filter(followup_model.imc_follow_up.id == id_to_find)

    def get_last_imc_data(self, dbSession: Session, id_user: int):
        return dbSession.query(followup_model.imc_follow_up).filter(followup_model.imc_follow_up.user_id == id_user).order_by(followup_model.imc_follow_up.date.desc()).first()

    def add_one_elem(self, body_followup_imc: followup_imc, dbSession: Session):
        if Session == None:
            return 'Null'

        newData = followup_model.imc_follow_up()
        newData.user_id = body_followup_imc.id_user
        newData.imc_computed = body_followup_imc.imc
        newData.weight = body_followup_imc.weight
        newData.date = body_followup_imc.date
        newData.day = body_followup_imc.date.day
        newData.month = body_followup_imc.date.month
        newData.year = body_followup_imc.date.year

        dbSession.add(newData)
        dbSession.commit()
        dbSession.refresh(newData)
        return newData


