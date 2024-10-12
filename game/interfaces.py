# game/interfaces.py

from abc import ABC, abstractmethod


class Movable(ABC):
    """Interface for movable objects."""

    @abstractmethod
    def move(self, dx: int, dy: int) -> None:
        pass


class Rotatable(ABC):
    """Interface for rotatable objects."""

    @abstractmethod
    def rotate(self) -> None:
        pass
