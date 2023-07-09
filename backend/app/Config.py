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

    class Config:
        env_file = ".env"


configs = Settings()
