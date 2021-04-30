from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import ARRAY

from ...database.base_class import Base


class medicine(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(Text)
    dose = Column(Integer)
    dose_max = Column(Integer)
    list_type = Column(ARRAY(Integer), nullable=True)
    list_symptoms = Column(ARRAY(Integer), nullable=True)
    delay = Column(Integer, nullable=True)
    active_principle = Column(ARRAY(Integer), nullable=True)
    list_excipients = Column(ARRAY(Integer), nullable=True)
    thumbnail_id = Column(Integer, nullable=True)


class medecineShort(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    description = Column(Text)
    dose = Column(Integer)
    dose_max = Column(Integer)


class thumbnail(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    img_name = Column(String)
    img_64 = Column(Text)
