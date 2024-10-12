# game/tetrominoes/tetromino_o.py

from game.tetromino import Tetromino
from game.enums import Color


class TetrominoO(Tetromino):
    """Class representing the 'O' shaped tetromino."""

    def __init__(self):
        """Initialize the O tetromino with its shape and color."""
        shape = [[1, 1], [1, 1]]
        super().__init__(shape, Color.YELLOW)

    def rotate(self) -> None:
        """Rotate the tetromino (O tetromino does not change on rotation)."""
        # The O tetromino does not change shape on rotation
        pass
