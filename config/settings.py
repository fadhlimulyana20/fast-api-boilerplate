from pydantic import BaseSettings


class Settings(BaseSettings):
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

setings = Settings()