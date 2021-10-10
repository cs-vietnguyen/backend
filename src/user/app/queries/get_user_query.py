from dataclasses import dataclass

from src.core.cqrs import Query, QueryHandler
from src.user.db.interactors import UserModelInteractor
from src.user.db.models import UserModel


@dataclass
class GetUserQuery(Query):
    user_id: str = ""
    username: str = ""

    def handler(self):
        return GetUserQueryHandler


class GetUserQueryHandler(QueryHandler):
    def handle(self, query: Query):
        super().handle(query)

        with self.db_context() as database_engine:
            if query.user_id:
                user: UserModel = UserModelInteractor.objects.get_user(
                    user_id=query.user_id, db=database_engine
                )
            elif query.username:
                user: UserModel = UserModelInteractor.objects.get_user_by_username(
                    username=query.username, db=database_engine
                )

            return user
