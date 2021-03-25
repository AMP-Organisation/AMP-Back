from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, ARRAY
from ...database.base_class import Base


class place(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    address = Column(VARCHAR(50))
    zip_code = Column(VARCHAR(15), nullable=False)
    department = Column(VARCHAR(50), nullable=False)
    region = Column(VARCHAR(50), nullable=False)
    country_code = Column(VARCHAR(10))
    type_id = Column(Integer, ForeignKey('place_type.id'), nullable=False)
    city = Column(VARCHAR(50), nullable=False)
    tags = Column(ARRAY(Integer))


class place_type(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    type = Column(VARCHAR(50), nullable=False)


class place_tags(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    type = Column(VARCHAR(50), nullable=False)
