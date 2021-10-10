from typing import Optional

from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.utils.security import VerifyAccessToken


class CustomBearerToken(HTTPBearer):
    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        authorization_credentials: Optional[
            HTTPAuthorizationCredentials
        ] = await super().__call__(request)

        return authorization_credentials.credentials  # type: ignore


def authorization(
    access_token: str = Depends(CustomBearerToken(auto_error=True))
):
    user_id: str = VerifyAccessToken(access_token=access_token).verify()

    return user_id
