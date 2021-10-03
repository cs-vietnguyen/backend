from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.settings import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
