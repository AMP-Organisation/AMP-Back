# File for the 
# Initialisation of the database connection
# made by Baptiste and Nathan
# March 21
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..core.settings import settings

# the database engine initialisation

database_url = settings.DATABASE_URL
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

dbEngine = create_engine(database_url, pool_pre_ping=True)
# the Dabatase Session : we use this variable to make the queries
dbSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=dbEngine)

# I have a problem using the other way created by my coworker
# a base class that our class wil derivate
dbBaseClass = declarative_base()
dbBaseClass.metadata.create_all(bind=dbEngine)