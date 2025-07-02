from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{settings.MYSQL_USERNAME}:{settings.MYSQL_PASS}"
    f"@{settings.MYSQL_HOSTNAME}:{settings.MYSQL_PORT}/{settings.MYSQL_DB_NAME}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=settings.MYSQL_POOL_PRE_PING,
    pool_size=settings.MYSQL_POOL_SIZE,
    max_overflow=settings.MYSQL_MAX_OVERFLOW,
    pool_timeout=settings.MYSQL_POOL_TIMEOUT,
    echo=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
