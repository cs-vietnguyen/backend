from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.utils import get_db
from src.user import schemas
from src.user.crud.user import create_user, get_user, get_user_by_username

router = APIRouter()


@router.get("/{user_id}", response_model=schemas.User)
def get(user_id: int, db: Session = Depends(get_db)) -> Any:
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=schemas.User)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)) -> Any:
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)