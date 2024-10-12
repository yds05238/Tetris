# game/input_handler.py

import pygame
from game.tetromino import Tetromino
from game.board import Board
from game.enums import Direction


class InputHandler:
    """Class to handle user inputs."""

    def process_events(self, events, tetromino: Tetromino, board: Board) -> bool:
        """
        Process input events.
        Args:
            events: List of Pygame events.
            tetromino (Tetromino): The current tetromino.
            board (Board): The game board.
        Returns:
            bool: False if the game should quit, True otherwise.
        """
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_tetromino(tetromino, board, Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.move_tetromino(tetromino, board, Direction.RIGHT)
                elif event.key == pygame.K_DOWN:
                    self.move_tetromino(tetromino, board, Direction.DOWN)
                elif event.key == pygame.K_UP:
                    self.rotate_tetromino(tetromino, board)
                elif event.key == pygame.K_SPACE:
                    self.hard_drop(tetromino, board)
        return True

    def move_tetromino(
        self, tetromino: Tetromino, board: Board, direction: Direction
    ) -> None:
        """Move tetromino in the specified direction."""
        dx, dy = 0, 0
        if direction == Direction.LEFT:
            dx = -1
        elif direction == Direction.RIGHT:
            dx = 1
        elif direction == Direction.DOWN:
            dy = 1
        new_position = tetromino.position.copy()
        new_position.x += dx
        new_position.y += dy
        if board.is_valid_position(tetromino, new_position):
            tetromino.move(dx, dy)

    def rotate_tetromino(self, tetromino: Tetromino, board: Board) -> None:
        """Rotate the tetromino."""
        original_shape = tetromino.shape.copy()
        tetromino.rotate()
        if not board.is_valid_position(tetromino, tetromino.position):
            # Revert rotation if invalid
            tetromino.shape = original_shape

    def hard_drop(self, tetromino: Tetromino, board: Board) -> None:
        """Drop the tetromino to the lowest valid position.

        Args:
            tetromino (Tetromino): The current tetromino.
            board (Board): The game board.
        """
        while board.is_valid_position(tetromino, tetromino.position.offset(0, 1)):
            tetromino.move(0, 1)
