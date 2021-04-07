from sqlalchemy import Column, Integer, VARCHAR
from ...database.base_class import Base


class Symptoms(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(VARCHAR(50), nullable=False, unique=True)
    danger = Column(Integer)
