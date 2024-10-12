# game/tetrominoes/tetromino_z.py

from game.tetromino import Tetromino
from game.enums import Color


class TetrominoZ(Tetromino):
    """Class representing the 'Z' shaped tetromino."""

    def __init__(self):
        """Initialize the Z tetromino with its shape and color."""
        shape = [[1, 1, 0], [0, 1, 1]]
        super().__init__(shape, Color.RED)

    def rotate(self) -> None:
        """Rotate the tetromino 90 degrees clockwise."""
        self._shape = [list(row) for row in zip(*self._shape[::-1])]
