from pydantic_settings import BaseSettings
from functools import lru_cache
import os


@lru_cache
def get_env_filename() -> str:
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    DB_URL: str
    ENVIRONMENT: str
    ALGORITHM: str
    JWT_SECRET: str
    
    class Config:
        env_file: str = get_env_filename()
        env_file_encoding: str = "utf-8"
        
        
@lru_cache
def get_env_vars() -> EnvironmentSettings:
    return EnvironmentSettings()
 