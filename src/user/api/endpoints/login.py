from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.core.cqrs import Bus
from src.user.app.queries import GetUserQuery
from src.user.db.models import UserModel
from src.user.schemas import UserSchemas
from src.utils import AccessToken, PasswordManager

router = APIRouter()

_bus: Bus = Bus()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()) -> UserSchemas:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user: UserModel = _bus.dispatch(GetUserQuery(username=form_data.username))
    if not user:
        raise HTTPException(status_code=400, detail="Username is wrong!")

    password_manager = PasswordManager(
        plain_password=form_data.password, hashed_password=user.password
    )
    if not password_manager.verify():
        raise HTTPException(status_code=400, detail="Password is wrong!")

    return {
        "access_token": AccessToken(sub=user.id).generate(),
        "token_type": "bearer",
    }
