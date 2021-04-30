from sqlalchemy import Column, Integer, VARCHAR
from ..base_class import Base


# Divide User in two model
# we don't need all the informations everytime

class Active_Ingredient(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(VARCHAR(50), nullable=False)
    max_dose_mg = Column(Integer, nullable=False)
