# score_manager.py


class ScoreManager:
    """Class to manage game scoring and levels."""

    def __init__(self):
        self._score = 0
        self._level = 1
        self._lines_cleared = 0

    @property
    def score(self) -> int:
        """Get the current score."""
        return self._score

    @property
    def level(self) -> int:
        """Get the current level."""
        return self._level

    @property
    def lines_cleared(self) -> int:
        """Get the number of lines cleared."""
        return self._lines_cleared

    def update_score(self, lines: int) -> None:
        """Update the score based on the number of lines cleared."""
        scoring = {1: 40, 2: 100, 3: 300, 4: 1200}
        self._score += scoring.get(lines, 0) * self._level
        self._lines_cleared += lines
        self._level = self._lines_cleared // 10 + 1
