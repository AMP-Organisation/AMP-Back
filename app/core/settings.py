import secrets
from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "toto"
    PROJECT_NAME: str = "amp-toto"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = "postgresql://Baptiste:bonjour2394@127.0.0.1/AMP"
    class Config:
        env_file = '.env'

settings = Settings()

