
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./sqlite.db"
    
    SECRET_KEY: str = "change me"
    ACCESS_EXPIRATION: int = 60  # 1 hour
    REFRESH_EXPIRATION: int = 10080  # 7 days


settings = Settings()
