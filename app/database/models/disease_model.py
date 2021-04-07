from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from .. import session


# So for the model, I derivate from the declarative base
# So I added this one too
# we can, with this way, create several class and derivate each from other
# in order to have tnier class with just data needed
class disease_base(session.dbBaseClass):
    __tablename__ = "disease"
    id = Column(Integer, primary_key=True, index=True)
    name_disease = Column(String)


class disease(disease_base):
    description = Column(String)
    is_vaccine = Column(Boolean)
    symptoms = Column(ARRAY(Integer))


class disease_more(disease):
    is_treatment = Column(Boolean)
    danger_level = Column(Integer)


class disease_type(session.dbBaseClass):
    __tablename__ = "disease_type"
    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String, unique=True)


# je n'ai pas le meme nom entre mon model et le schema et donc je converti les données...
class convertSchemaToModel:
    dmodel = disease_more()

    def __init__(self, schemaToConvert):
        print("convert schema to model")
        print(schemaToConvert)
        self.dmodel.id = schemaToConvert['id']
        self.dmodel.name_disease = schemaToConvert['name']
        self.dmodel.description = schemaToConvert['description']
        self.dmodel.is_vaccine = schemaToConvert['is_vaccine']
        self.dmodel.symptoms = schemaToConvert['symptoms']
        self.dmodel.danger_level = schemaToConvert['danger_level']
        self.dmodel.is_treatment = schemaToConvert['is_treatment']

    def get_converted(self):
        return self.dmodel
