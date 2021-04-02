from sqlalchemy.orm import Session 
from fastapi.encoders import jsonable_encoder

from ..database.models import disease_model

class CRUD_disease:
    # I set a limit to 100 by default
    def get_all_disease(self, dbSession: Session, limit: int = 100):
        return dbSession.query(disease_model.disease).limit(limit).all()

    # not finished : to paginate the disease
    def get_all_disease_pages(self, dbSession: Session, limit: int = 100):
        return dbSession.query(disease_model.disease).limit(limit).all()

    # get only one disease according to the id, but with more data than the all query
    def get_one_disease(self, dbSession: Session, id_to_find: int):
        return dbSession.query(disease_model.disease_more).filter(disease_model.disease_more.id == id_to_find).first()

    def get_all_disease_type(self, dbSession: Session, limit: int = 10):
        return dbSession.query(disease_model.disease_type).limit(limit).all()

    # I think I can easily refactor that 
    def add_a_disease(self, dbSession: Session, data_to_add: disease_model.disease_more):
        new_disease = disease_model.disease_more()
        new_disease.name_disease = data_to_add.name
        new_disease.description = data_to_add.description
        new_disease.is_vaccine = data_to_add.is_vaccine
        new_disease.is_treatment = data_to_add.is_treatment
        new_disease.danger_level = data_to_add.danger_level
        dbSession.add(new_disease)
        dbSession.commit()
        dbSession.refresh(new_disease)
        return new_disease

    # for now, PATCH only work on descriptioon and name
    def patch_a_disease(self, dbSession: Session, data_to_up: disease_model.disease, id_dis: int):
        dis_to_patch = dbSession.query(disease_model.disease_more).filter(disease_model.disease_more.id == data_to_up.id).first()
        dis_to_patch.name_disease = data_to_up.name if data_to_up.name != None else dis_to_patch.name_disease
        dis_to_patch.description = data_to_up.description if data_to_up.description != None else dis_to_patch.description
        dbSession.commit()
        patched = dbSession.query(disease_model.disease_more).filter(disease_model.disease_more.id == data_to_up.id).first()
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

    def delete_disease(self, dbSession: Session, id_disease: int):
        disease_to_del = dbSession.query(disease_model.disease_base).filter(disease_model.disease_base.id == id_disease).first()
        dbSession.delete(disease_to_del)
        dbSession.commit()
        return disease_to_del