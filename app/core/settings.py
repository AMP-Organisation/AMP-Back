import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    PROJECT_NAME: str = 'AMP-BACK'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URL: str = 'postgresql://postgres:password@localhost:5432/amp'

    class Config:
        env_file = '.env'


settings = Settings()
