import inspect
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Optional, Union

from src.db.database_context import DatabaseContextManager


class ActionName(Enum):
    query: str = "Query"
    command: str = "Command"


class Action(ABC):
    @property
    def _handler(self):
        try:
            return getattr(
                self._getmodule(), self.__class__.__name__ + "Handler"
            )
        except AttributeError:
            return None

    def _getmodule(self):
        return inspect.getmodule(self)

    @abstractmethod
    def handler(self):
        pass


class Query(Action):
    def handler(self):
        return super()._handler


class Command(Action):
    def handler(self):
        return super()._handler


class Handler(ABC):
    name: str
    db_context: DatabaseContextManager = DatabaseContextManager  # type: ignore

    def handle(self, action: Action):
        # logger.info(f"Dispatching a {self.name}...")
        # logger.info(f"{self.__class__.__name__} executing {action.__class__.__name__}!")
        pass


class QueryHandler(Handler):
    name: str = ActionName.query.value

    def handle(self, query: Union[Action, Query]):
        return super().handle(query)


class CommandHandler(Handler):
    name: str = ActionName.command.value

    def handle(self, command: Union[Action, Command]):
        return super().handle(command)


class Resolver:
    def execute(self, action: Action):
        handler: Handler = self.lookup_handler(action)
        return handler.handle(action)

    def lookup_handler(self, action: Action):
        handler: Handler = action.handler()
        if handler is not None:
            return handler()  # type: ignore


class Bus:
    resolver: Resolver = Resolver()

    def dispatch(self, action: Action):
        action_result: Optional[Any] = self.resolver.execute(action)
        return action_result


if __name__ == "__main__":
    test_query = Query()
    bus = Bus()
    bus.dispatch(test_query)
