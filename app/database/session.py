# File for the 
# Initialisation of the database connection
# made by Baptiste and Nathan
# March 21
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..core.settings import settings

# the database engine initialisation
dbEngine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
# the Dabatase Session : we use this variable to make the queries
dbSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=dbEngine)

