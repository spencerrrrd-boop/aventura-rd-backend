from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    SSL_MODE: str = "REQUIRED"
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    APP_NAME: str = "AventuraRD API"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()