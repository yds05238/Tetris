# game/tetromino_factory.py

import random
from game.tetromino import Tetromino
from game.tetrominoes.tetromino_i import TetrominoI
from game.tetrominoes.tetromino_o import TetrominoO
from game.tetrominoes.tetromino_j import TetrominoJ
from game.tetrominoes.tetromino_l import TetrominoL
from game.tetrominoes.tetromino_s import TetrominoS
from game.tetrominoes.tetromino_t import TetrominoT
from game.tetrominoes.tetromino_z import TetrominoZ


class TetrominoFactory:
    """Factory to create tetromino instances."""

    def __init__(self):
        """Initialize the tetromino factory with a list of tetromino classes."""
        self.tetromino_classes = [
            TetrominoI,
            TetrominoO,
            TetrominoJ,
            TetrominoL,
            TetrominoS,
            TetrominoT,
            TetrominoZ,
        ]

    def get_random_tetromino(self) -> Tetromino:
        """Return a new random tetromino instance."""
        tetromino_class = random.choice(self.tetromino_classes)
        return tetromino_class()
