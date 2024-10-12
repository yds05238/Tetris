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
        """Rotate the tetromino clockwise (no effect for 'O')."""
        pass

    def rotate_counter_clockwise(self) -> None:
        """Rotate the tetromino counter-clockwise (no effect for 'O')."""
        pass
