from dataclasses import dataclass

from fastapi import HTTPException

from src.core.cqrs import Command, CommandHandler
from src.user.db.interactors import UserModelInteractor
from src.user.db.models import UserModel
from src.user.schemas import UserCreate
from src.utils import PasswordManager


@dataclass
class CreateUserCommand(Command):
    user: UserCreate

    def handler(self):
        return CreateUserCommandHandler


class CreateUserCommandHandler(CommandHandler):
    def handle(self, command: Command):
        with self.db_context() as database_engine:
            user: UserModel = UserModelInteractor.objects.get_user_by_username(
                username=command.user.username, db=database_engine
            )
            if user:
                raise HTTPException(
                    status_code=400, detail="Email already registered"
                )
            command.user.password = PasswordManager(
                plain_password=command.user.password
            ).generate()

            return UserModelInteractor.objects.create(
                obj=command.user, db=database_engine
            )
