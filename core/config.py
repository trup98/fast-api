from pydantic import BaseSettings

class Settings(BaseSettings):
    MYSQL_HOSTNAME: str
    MYSQL_USERNAME: str
    MYSQL_PASS: str
    MYSQL_PORT: int
    MYSQL_DB_NAME: str

    MYSQL_POOL_SIZE: int = 5
    MYSQL_MAX_OVERFLOW: int = 10
    MYSQL_POOL_TIMEOUT: int = 30
    MYSQL_POOL_PRE_PING: bool = True

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
