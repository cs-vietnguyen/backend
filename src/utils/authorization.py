from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.core.settings import settings
from src.utils.security import VerifyAccessToken

oauth2_bearer = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/users/login"
)


def authorization(access_token: str = Depends(oauth2_bearer)):
    user_id: str = VerifyAccessToken(access_token=access_token).verify()

    return user_id
