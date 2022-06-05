from typing import List, Callable
from abc import ABC, abstractmethod

from melee import Controller, GameState


Action = Callable[[Controller], None]


def no_op(controller: Controller) -> None:
    return None


class ActionQueue:

    def __init__(self):
        self._queue = list()

    def push(self, action: Action) -> None:
        self._queue.insert(0, action)

    def pop(self) -> Action:
        if not self._queue:
            return no_op
        return self._queue.pop()

    def clear(self):
        self._queue.clear()


class Actuator(ABC):
    @abstractmethod
    def to_action(self, state: GameState) -> List[Action]:
        pass

    def _no_ops(self, count: int) -> List[Action]:
        return [no_op] * count
