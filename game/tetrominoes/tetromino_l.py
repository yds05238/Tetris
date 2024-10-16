# game/tetrominoes/tetromino_l.py

from game.tetromino import Tetromino
from game.enums import Color


class TetrominoL(Tetromino):
    """Class representing the 'L' shaped tetromino."""

    def __init__(self):
        """Initialize the L tetromino with its shape and color."""
        shape = [[0, 0, 1], [1, 1, 1]]
        super().__init__(shape, Color.ORANGE)
