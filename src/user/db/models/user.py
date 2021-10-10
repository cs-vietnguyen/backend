from sqlalchemy import Boolean, Column, String

from src.db.base_model import Base
from src.utils.generator import primary_key


class User(Base):
    id = Column(
        String(36),
        unique=True,
        primary_key=True,
        index=True,
        default=primary_key,
    )
    full_name = Column(String(length=50), default="")
    phone_number = Column(String(length=20), default="", onupdate="")
    username = Column(String(length=50), unique=True, index=True)
    password = Column(String(length=100), nullable=False)
    is_active = Column(Boolean(), default=True)
