from pydantic import BaseSettings, AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    database_url: str
    redis_url: str
    secret_key: str
    jwt_expires_minutes: int = 60
    backend_cors_origins: List[AnyHttpUrl] = []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
