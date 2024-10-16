# game/tetrominoes/tetromino_s.py

from game.tetromino import Tetromino
from game.enums import Color


class TetrominoS(Tetromino):
    """Class representing the 'S' shaped tetromino."""

    def __init__(self):
        """Initialize the S tetromino with its shape and color."""
        shape = [[0, 1, 1], [1, 1, 0]]
        super().__init__(shape, Color.GREEN)
