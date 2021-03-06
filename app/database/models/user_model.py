from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP, ForeignKey, Float
from ..base_class import Base


# Divide User in two model
# we don't need all the informations everytime

class Users(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    last_name = Column(VARCHAR(50), nullable=False)
    first_name = Column(VARCHAR(50), nullable=False)
    email = Column(VARCHAR, nullable=False)
    username = Column(VARCHAR, nullable=False)
    age = Column(Integer)
    birth_date = Column(TIMESTAMP, nullable=False)
    dt_inscription = Column(TIMESTAMP, nullable=False)
    last_login = Column(TIMESTAMP)
    password = Column(VARCHAR(100), unique=True)
    fk_group = Column(Integer, ForeignKey('group.id'))
    height = Column(Float)


class Group(Base):
    id = Column(Integer, primary_key=True, index=True)
    Type = Column(VARCHAR(50))
