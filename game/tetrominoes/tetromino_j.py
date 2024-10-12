from game.tetromino import Tetromino
from game.enums import Color


class TetrominoJ(Tetromino):
    """Class representing the 'J' shaped tetromino."""

    def __init__(self):
        shape = [[1, 0, 0], [1, 1, 1]]
        super().__init__(shape, Color.CYAN)
