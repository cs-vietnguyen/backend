from sqlalchemy.orm import Session  # noqa

from src.user import schemas
from src.user.db.models.user import User as UserModel


def get_user(db: Session, user_id: int) -> UserModel:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> UserModel:
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> UserModel:
    fake_password = user.password + "notreallyhashed"
    db_user = UserModel(username=user.username, password=fake_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
