from fastapi import APIRouter

from user.api.endpoints import login, users

router = APIRouter()

router.include_router(login.router, prefix="/users")
router.include_router(users.router, prefix="/users")
