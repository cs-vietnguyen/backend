from dependency_injector import containers, providers

from src.user.db.managers import UserManager
from src.user.db.models.user import User


class UserModelInteractor(containers.DeclarativeContainer):
    model: User = providers.Factory(User)
    objects: UserManager = providers.Singleton(UserManager, User)()
