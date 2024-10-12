# game/enums.py

from enum import Enum, auto


class Color(Enum):
    """Enumeration for colors used in the game."""

    EMPTY = "EMPTY"
    CYAN = "CYAN"
    YELLOW = "YELLOW"
    PURPLE = "PURPLE"
    GREEN = "GREEN"
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"


class Direction(Enum):
    """Enumeration for movement directions."""

    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()
    UP = auto()
