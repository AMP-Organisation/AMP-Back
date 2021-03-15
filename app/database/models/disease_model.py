from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from .. import session
from .. import base_class

class disease_base(session.dbBaseClass):
    __tablename__ = "disease"
    id = Column(Integer, primary_key=True, index=True)
    name_disease = Column(String)

class disease(disease_base):
    description = Column(String)
    is_vaccine = Column(Boolean)

class disease_type(session.dbBaseClass):
    __tablename__ = "disease_type"
    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String, unique=True)