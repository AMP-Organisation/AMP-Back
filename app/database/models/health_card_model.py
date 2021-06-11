from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, ARRAY
from ...database.base_class import Base


class health_card(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    allergy = Column(ARRAY(Integer))
    blood_group = Column(VARCHAR(10))
    disease = Column(ARRAY(Integer))
    user_id = Column(Integer, ForeignKey('users.id'))
