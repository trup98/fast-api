from sqlalchemy import Column, Integer, String
from db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    first_name = Column(String(100), unique=True, index=True, nullable=False)
    last_name = Column(String(100), unique=True, index=True, nullable=False)
