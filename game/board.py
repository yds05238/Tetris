# game/board.py

from game.enums import Color
from game.tetromino import Tetromino
from game.position import Position
from constants import GRID_WIDTH, GRID_HEIGHT


class Board:
    """Class representing the Tetris game board."""

    def __init__(self):
        """Initialize the board grid."""
        self._width = GRID_WIDTH
        self._height = GRID_HEIGHT
        self._grid: list[list[Color]] = [
            [Color.EMPTY for _ in range(self._width)] for _ in range(self._height)
        ]

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def grid(self) -> list[list[Color]]:
        return self._grid

    def is_valid_position(self, tetromino: Tetromino, position: Position) -> bool:
        """
        Check if the tetromino can be placed at the given position.
        Args:
            tetromino (Tetromino): The tetromino to check.
            position (Position): The position to check.
        Returns:
            bool: True if valid, False otherwise.
        """
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = position.x + x
                    new_y = position.y + y
                    if (
                        new_x < 0
                        or new_x >= self._width
                        or new_y < 0
                        or new_y >= self._height
                        or self._grid[new_y][new_x] != Color.EMPTY
                    ):
                        return False
        return True

    def place_tetromino(self, tetromino: Tetromino) -> None:
        """Place the tetromino onto the board grid."""
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = tetromino.position.x + x
                    grid_y = tetromino.position.y + y
                    self._grid[grid_y][grid_x] = tetromino.color

    def clear_lines(self) -> int:
        """Clear completed lines from the board. Returns the number of lines cleared."""
        new_grid = [
            row for row in self._grid if any(cell == Color.EMPTY for cell in row)
        ]
        lines_cleared = self._height - len(new_grid)
        while len(new_grid) < self._height:
            new_grid.insert(0, [Color.EMPTY for _ in range(self._width)])
        self._grid = new_grid
        return lines_cleared
