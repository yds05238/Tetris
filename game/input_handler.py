# game/input_handler.py

import pygame
from game.tetromino import Tetromino
from game.board import Board
from game.enums import Direction


class InputHandler:
    """Class to handle user inputs."""

    def process_home_screen_events(self, events, game) -> bool:
        """Process input events on the home screen.

        Args:
            events: List of Pygame events.
            game (Game): The game instance.

        Returns:
            bool: False if the game should quit, True otherwise.
        """
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.start_game()
        return True

    def process_events(self, events, tetromino: Tetromino, board: Board) -> bool:
        """Process input events during the game.

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
                elif event.key == pygame.K_z:
                    self.rotate_tetromino_counter_clockwise(tetromino, board)
                elif event.key == pygame.K_SPACE:
                    self.hard_drop(tetromino, board)

            # Handle other events as needed

        return True

    def process_game_over_events(self, events, game) -> bool:
        """Process input events on the game over screen.

        Args:
            events: List of Pygame events.
            game (Game): The game instance.

        Returns:
            bool: False if the game should quit, True otherwise.
        """
        for event in events:
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.start_game()  # Restart the game
                elif event.key == pygame.K_q:
                    return False
        return True

    def move_tetromino(
        self, tetromino: Tetromino, board: Board, direction: Direction
    ) -> None:
        """Move the tetromino in the specified direction.

        Args:
            tetromino (Tetromino): The tetromino to move.
            board (Board): The game board.
            direction (Direction): The direction to move.
        """
        dx, dy = 0, 0
        if direction == Direction.LEFT:
            dx = -1
        elif direction == Direction.RIGHT:
            dx = 1
        elif direction == Direction.DOWN:
            dy = 1
        new_position = tetromino.position.offset(dx, dy)
        if board.is_valid_position(tetromino, new_position):
            tetromino.move(dx, dy)

    def rotate_tetromino(self, tetromino: Tetromino, board: Board) -> None:
        """Rotate the tetromino clockwise.

        Args:
            tetromino (Tetromino): The tetromino to rotate.
            board (Board): The game board.
        """
        original_shape = [row[:] for row in tetromino.shape]
        tetromino.rotate()
        if not board.is_valid_position(tetromino, tetromino.position):
            tetromino.shape = original_shape

    def rotate_tetromino_counter_clockwise(
        self, tetromino: Tetromino, board: Board
    ) -> None:
        """Rotate the tetromino counter-clockwise.

        Args:
            tetromino (Tetromino): The tetromino to rotate.
            board (Board): The game board.
        """
        original_shape = [row[:] for row in tetromino.shape]
        tetromino.rotate_counter_clockwise()
        if not board.is_valid_position(tetromino, tetromino.position):
            tetromino.shape = original_shape

    def hard_drop(self, tetromino: Tetromino, board: Board) -> None:
        """Drop the tetromino to the lowest valid position.

        Args:
            tetromino (Tetromino): The tetromino to drop.
            board (Board): The game board.
        """
        while board.is_valid_position(tetromino, tetromino.position.offset(0, 1)):
            tetromino.move(0, 1)
