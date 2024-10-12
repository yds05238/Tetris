# game/enums.py

from enum import Enum


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

    LEFT = "LEFT"
    RIGHT = "RIGHT"
    DOWN = "DOWN"
    UP = "UP"


class GameState(Enum):
    """Enumeration for the game states."""

    HOME_SCREEN = "HOME_SCREEN"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    GAME_OVER = "GAME_OVER"
