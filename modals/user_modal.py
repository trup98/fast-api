from email.policy import default

from sqlalchemy import Column, Integer, String, Boolean
from db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100))
    email = Column(String(100), unique=True, index=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=True)
