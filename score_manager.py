# score_manager.py


class ScoreManager:
    """Class to manage game scoring and levels."""

    def __init__(self):
        self._lines_cleared = 0
        self._level = 1

    @property
    def level(self) -> int:
        """Get the current level."""
        return self._level

    @property
    def lines_cleared(self) -> int:
        """Get the number of lines cleared."""
        return self._lines_cleared

    def update_lines_cleared(self, lines: int) -> None:
        """Update the total number of lines cleared.

        Args:
            lines (int): The number of lines cleared.
        """
        self._lines_cleared += lines
        self.update_level()

    def update_level(self) -> None:
        """Update the game level based on lines cleared."""
        # Increase level every 10 lines cleared (optional)
        self._level = self._lines_cleared // 10 + 1
