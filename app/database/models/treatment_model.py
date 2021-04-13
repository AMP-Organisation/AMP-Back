from sqlalchemy import Column, Integer, VARCHAR, Text, TIMESTAMP, ForeignKey
from ...database.base_class import Base


class Treatment(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(VARCHAR(50), nullable=False)
    description = Column(Text)
    medicine_id = Column(Integer, ForeignKey('medicine.id'))
    beginning_date = Column(TIMESTAMP, nullable=False)
    ending_date = Column(TIMESTAMP)
