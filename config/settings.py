from functools import lru_cache
from pydantic import BaseSettings


class Env(BaseSettings):
    env: str

    app_name: str = "FAST API"
    admin_email: str

    # Database
    db_driver: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_env():
    return Env()