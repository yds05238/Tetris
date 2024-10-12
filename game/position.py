# game/position.py


class Position:
    """Class representing a position on the grid."""

    def __init__(self, x: int, y: int):
        """Initialize a position.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        self.x = x
        self.y = y

    def copy(self) -> "Position":
        """Create a copy of the position.

        Returns:
            Position: A new Position object with the same coordinates.
        """
        return Position(self.x, self.y)

    def move(self, dx: int, dy: int) -> None:
        """Move the position by dx and dy.

        Args:
            dx (int): Change in x-coordinate.
            dy (int): Change in y-coordinate.
        """
        self.x += dx
        self.y += dy

    def offset(self, dx: int, dy: int) -> "Position":
        """Return a new Position offset by dx and dy.

        Args:
            dx (int): Offset in x-coordinate.
            dy (int): Offset in y-coordinate.

        Returns:
            Position: A new Position object offset by dx and dy.
        """
        return Position(self.x + dx, self.y + dy)
