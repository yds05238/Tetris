# game/tetromino.py

from abc import ABC, abstractmethod
from typing import List
from game.position import Position
from game.enums import Color
from game.interfaces import Movable, Rotatable


class Tetromino(Movable, Rotatable, ABC):
    """Abstract base class for tetromino shapes."""

    def __init__(self, shape: List[List[int]], color: Color):
        """
        Initialize a tetromino.
        Args:
            shape (List[List[int]]): The shape matrix of the tetromino.
            color (Color): The color of the tetromino.
        """
        self._shape = shape
        self._color = color
        self._position = Position(0, 0)

    @property
    def shape(self) -> List[List[int]]:
        """Get the shape of the tetromino."""
        return self._shape

    @property
    def color(self) -> Color:
        """Get the color of the tetromino."""
        return self._color

    @property
    def position(self) -> Position:
        """Get the position of the tetromino."""
        return self._position

    @position.setter
    def position(self, position: Position) -> None:
        """Set the position of the tetromino."""
        self._position = position

    def move(self, dx: int, dy: int) -> None:
        """Move the tetromino by dx and dy."""
        self._position.x += dx
        self._position.y += dy

    @abstractmethod
    def rotate(self) -> None:
        """Rotate the tetromino."""
        pass
