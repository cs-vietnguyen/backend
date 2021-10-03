from fastapi import APIRouter

from user.api import routers as user_routers

router = APIRouter()

router.include_router(user_routers.router)
