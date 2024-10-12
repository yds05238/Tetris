# game/tetrominoes/tetromino_i.py

from game.tetromino import Tetromino
from game.enums import Color


class TetrominoI(Tetromino):
    """Class representing the 'I' shaped tetromino."""

    def __init__(self):
        shape = [[1, 1, 1, 1]]
        super().__init__(shape, Color.CYAN)
