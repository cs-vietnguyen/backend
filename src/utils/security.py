import time
import uuid
from dataclasses import dataclass
from typing import Dict, Optional

from authlib.jose import jwt
from passlib.context import CryptContext

from src.core.settings import settings

ACCESS_TOKEN_DURATION = 86400 * 365


class AccessToken:
    def __init__(self, sub: str) -> None:
        self.sub = sub

    def generate(self):
        current_time = self.current_time()
        expire_time = self.expire_time(current_time)
        payload = {
            "sub": self.sub,
            "exp": expire_time,
            "iat": current_time,
            "jti": str(uuid.uuid4()),
        }
        return jwt.encode(
            settings.JWT_HEADER, payload, settings.JWT_PRIVATE_SIGNATURE
        ).decode("utf-8")

    def current_time(self):
        return int(time.time())

    def expire_time(self, timeline):
        return timeline + ACCESS_TOKEN_DURATION


class VerifyAccessToken:
    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    def verify(self):
        try:
            infors: Dict = jwt.decode(
                self.access_token, settings.JWT_PRIVATE_SIGNATURE
            )
        except Exception as ex:
            raise ex

        return infors["sub"]


@dataclass
class PasswordManager:
    plain_password: str
    hashed_password: Optional[str] = None

    cryptor: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def generate(self):
        return self.cryptor.hash(self.plain_password)

    def verify(self):
        if not self.hashed_password:
            return False

        return self.cryptor.verify(self.plain_password, self.hashed_password)
