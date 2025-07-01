import logging
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv(override=True)

class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    @property
    def async_database_url(self) -> str:
        print(f"======== host:{self.DB_HOST}; port:{self.DB_PORT} ========")
        return (
        f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
