from typing import Generator
from ..database.session import dbSessionLocal

def get_db() -> Generator:
    try:
        db = dbSessionLocal()
        yield db
    finally:
        db.close()