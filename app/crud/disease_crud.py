from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder

from ..database.models import disease_model

class CRUD_disease:
# j'ai remis une limite a 100 ici meme si plus en amont j'ai mis 10 
    def get_all_disease(self, dbSession: Session, limit: int = 100):
        return dbSession.query(disease_model.disease).limit(limit).all()

    def get_all_disease_pages(self, dbSession: Session, limit: int = 100):
        return dbSession.query(disease_model.disease).limit(limit).all()

    # get only one disease according to the id, but with more data than the all query
    def get_one_disease(self, dbSession: Session, id_to_find: int):
        return dbSession.query(disease_model.disease_more).filter(disease_model.disease_more.id == id_to_find).first()

    def get_all_disease_type(self, dbSession: Session, limit: int = 10):
        return dbSession.query(disease_model.disease_type).limit(limit).all()

    def add_a_disease(self, dbSession: Session, data_to_add: disease_model.disease_more):
        new_disease = disease_model.disease_more()
        new_disease.name_disease = data_to_add.name
        new_disease.description = data_to_add.description
        new_disease.is_vaccine = data_to_add.is_vaccine
        new_disease.is_treatment = data_to_add.is_treatment
        new_disease.danger_level = data_to_add.danger_level
        print("new disease")
        print(new_disease)
        print(new_disease.id)
        print(new_disease.is_treatment )
        print(new_disease.danger_level)
        dbSession.add(new_disease)
        dbSession.commit()
        dbSession.refresh(new_disease)
        return new_disease

    def patch_a_disease(self, dbSession: Session, data_to_up: disease_model.disease, id_dis: int):
        print("data_to_up ")
        print(data_to_up.id)
        print(data_to_up.name)
        print(data_to_up.description)
        print(data_to_up.is_vaccine)
        print(data_to_up.is_treatment)
        print(data_to_up.danger_level)

        dis_to_patch = dbSession.query(disease_model.disease_more).filter(disease_model.disease_more.id == data_to_up.id).first()
        dis_to_patch.name_disease = data_to_up.name if data_to_up.name != None else dis_to_patch.name_disease
        dis_to_patch.description = data_to_up.description if data_to_up.description != None else dis_to_patch.description
        print("data found")
        print(dis_to_patch)
        print(dis_to_patch.name_disease)
        print(dis_to_patch.description)
        print(dbSession.dirty)
        dbSession.commit()
        patched = dbSession.query(disease_model.disease_more).filter(disease_model.disease_more.id == data_to_up.id).first()
        #return "patch in progress"
        return patched

    # A refactoriser !
    # probleme de nom de champ, j'ai du faire une sorte de converter
    def update_disease(self, dbSession: Session, data_to_up: disease_model.disease):
        data_encoded = jsonable_encoder(data_to_up)
        print("data pydantic converti en json")
        print(data_encoded)
        print(data_encoded['id'])
        converter = disease_model.convertSchemaToModel(data_encoded)
        converted = converter.get_converted()
        print("converted")
        print(converted.name_disease)
        converted.id = None

        disease_to_del = dbSession.query(disease_model.disease_base).filter(disease_model.disease_base.id == data_encoded['id']).first()
        print("celle a supp avant")
        print(disease_to_del)
        dbSession.delete(disease_to_del)

        dbSession.add(converted)
        dbSession.commit()
        dbSession.refresh(converted)
        return converted
        #return "in progress"

    def delete_disease(self, dbSession: Session, id_disease: int):
        disease_to_del = dbSession.query(disease_model.disease_base).filter(disease_model.disease_base.id == id_disease).first()
        dbSession.delete(disease_to_del)
        dbSession.commit()
        return disease_to_del