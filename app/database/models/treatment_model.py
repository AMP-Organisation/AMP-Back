from sqlalchemy import Column, Integer, VARCHAR, Text, TIMESTAMP, ForeignKey, ARRAY
from ...database.base_class import Base


class Treatment(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(Text)
    medicine_id = Column(ARRAY(Integer))
    beginning_date = Column(TIMESTAMP, nullable=False)
    ending_date = Column(TIMESTAMP)
