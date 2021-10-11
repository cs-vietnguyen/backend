from fastapi import APIRouter

from src.core.settings import settings
from user.api import routers as user_routers

router = APIRouter(tags=["Specification Documentation"])

router.include_router(user_routers.router, prefix=settings.API_V1_STR)
