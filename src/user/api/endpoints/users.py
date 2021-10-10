from fastapi import APIRouter, Depends, HTTPException

from src.core.cqrs import Bus
from src.user.app.commands import CreateUserCommand
from src.user.app.queries import GetUserQuery
from src.user.db.models import UserModel
from src.user.schemas import UserCreate, UserSchemas
from src.utils import authorization

router = APIRouter()

_bus: Bus = Bus()


@router.get("/profile", response_model=UserSchemas)
def get(user_id: str = Depends(authorization)) -> UserSchemas:
    user: UserModel = _bus.dispatch(GetUserQuery(user_id=user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserSchemas)
def create(user: UserCreate) -> UserSchemas:
    new_user: UserModel = _bus.dispatch(CreateUserCommand(user=user))
    return new_user
