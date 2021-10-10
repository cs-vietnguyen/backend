from sqlalchemy.orm import Session

from src.db.base_model import Base
from src.db.manager import Manager


class UserManager(Manager):
    def get_user(self, user_id: int, db: Session) -> Base:
        return db.query(self.model).filter(self.model.id == user_id).first()

    def get_user_by_username(self, username: str, db: Session) -> Base:
        return (
            db.query(self.model)
            .filter(self.model.username == username)
            .first()
        )

    def get_users(self, db: Session, skip: int = 0, limit: int = 100) -> Base:
        return db.query(self.model).offset(skip).limit(limit).all()
