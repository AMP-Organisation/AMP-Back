from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY

from ...database.base_class import Base

# rappel, c'est le model des données renvoyées depuis la bdd

# le nom sera a changer (?)
class imc_follow_up(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer)
    weight = Column(Integer)
    date = Column(TIMESTAMP, nullable=False)
    imc_computed = Column(Integer)
    day = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
