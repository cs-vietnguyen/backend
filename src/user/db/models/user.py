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
    full_name = Column(String(50))
    username = Column(String(50), unique=True, index=True)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean(), default=True)
