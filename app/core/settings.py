

import secrets
from pydantic import BaseSettings
class Settings(BaseSettings):
    API_V1_STR: str
    PROJECT_NAME: str
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str
    class Config:
        env_file = '.env'
settings = Settings()

