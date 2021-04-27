from sqlalchemy import Column, Integer, VARCHAR, Text, TIMESTAMP, ForeignKey, ARRAY
from ...database.base_class import Base


class Pillbox(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(Text)
    beginning_date = Column(TIMESTAMP, nullable=False)
    ending_date = Column(TIMESTAMP)
    list_treatment = Column(ARRAY(Integer), nullable=False)
    user_id = Column(Integer, ForeignKey('treatment.id'))
