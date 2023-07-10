from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Environment variables automatic parser.
    """
    APP_NAME: Optional[str] = None
    APP_VERSION: Optional[str] = None
    PORT: Optional[int] = 8009
    MONGO_DB_URI: Optional[str] = None
    MONGO_DBNAME: Optional[str] = None
    PYTHON_ENV: Optional[str] = None
    SECRET_KEY: Optional[str] = None
    ALGORITHM: Optional[str] = None
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = 0
    DEFAULT_ADMIN_EMAIL: Optional[str] = None
    DEFAULT_ADMIN_PASSWORD: Optional[str] = None
    DEFAULT_ADMIN_NAME: Optional[str] = None

    class Config:
        env_file = ".env"


configs = Settings()
