# game/tetrominoes/tetromino_t.py

from game.tetromino import Tetromino
from game.enums import Color


class TetrominoT(Tetromino):
    """Class representing the 'T' shaped tetromino."""

    def __init__(self):
        """Initialize the T tetromino with its shape and color."""
        shape = [[0, 1, 0], [1, 1, 1]]
        super().__init__(shape, Color.PURPLE)
