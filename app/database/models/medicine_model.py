from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from .. import session
from ...database.base_class import Base

class medicine(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    dose = Column(Integer)
    dose_max = Column(Integer)
    list_type = Column(ARRAY(Integer))
    list_symptoms = Column(ARRAY(Integer))
    delay = Column(Integer)
    active_principle = Column(ARRAY(Integer))
    list_excipients = Column(ARRAY(Integer))