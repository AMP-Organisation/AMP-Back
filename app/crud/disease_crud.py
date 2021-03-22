from sqlalchemy.orm import Session 

from ..database.models import disease_model

class CRUD_disease:
# j'ai remis une limite a 100 ici meme si plus en amont j'ai mis 10 
    def get_all_disease(self, dbSession: Session, limit: int = 100):
        return dbSession.query(disease_model.disease).limit(limit).all()

    def get_one_disease(self, dbSession: Session, id_to_find: int):
        return dbSession.query(disease_model.disease).filter(disease_model.disease_base.id == id_to_find).first()

    def get_all_disease_type(self, dbSession: Session, limit: int = 10):
        return dbSession.query(disease_model.disease_type).limit(limit).all()

    def add_a_disease(self, dbSession: Session, data_to_add: disease_model.disease):
        new_disease = disease_model.disease()
        new_disease.name_disease = data_to_add.name
        new_disease.description = data_to_add.description
        new_disease.is_vaccine = data_to_add.is_vaccine

        dbSession.add(new_disease)
        dbSession.commit()
        dbSession.refresh(new_disease)
        return new_disease

    def update_disease(self, dbSession: Session, data_to_up: disease_model.disease):
        
        return "in progress"

    def delete_disease(self, dbSession: Session, id_disease: int):
        disease_to_del = dbSession.query(disease_model.disease_base).filter(disease_model.disease_base.id == id_disease).first()
        dbSession.delete(disease_to_del)
        dbSession.commit()
        return disease_to_del