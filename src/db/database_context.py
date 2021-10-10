from sqlalchemy.orm import Session

from src.db.session import SessionLocal


def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


class DatabaseContextManager:
    def __init__(self):
        self.db: Session = get_db()

    def __enter__(self):
        return next(self.db)

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()
