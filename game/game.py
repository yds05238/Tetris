# game/game.py

import pygame
import time
from game.board import Board
from game.tetromino_factory import TetrominoFactory
from score_manager import ScoreManager
from game.renderer import Renderer
from game.input_handler import InputHandler
from game.position import Position
from constants import (
    GRID_WIDTH,
    GRID_HEIGHT,
    CELL_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    DROP_INTERVAL,
    COLORS,
)
from game.enums import Direction, Color
from game.tetromino import Tetromino


class Game:
    """Main class to control the game flow."""

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.tetromino_factory = TetrominoFactory()
        self.score_manager = ScoreManager()
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler()
        self.current_tetromino = self.get_new_tetromino()
        self.is_game_over = False
        self.last_drop_time = pygame.time.get_ticks()
        self.drop_interval = DROP_INTERVAL

    def get_new_tetromino(self) -> Tetromino:
        """Generate a new tetromino."""
        tetromino = self.tetromino_factory.get_random_tetromino()
        tetromino.position = Position(GRID_WIDTH // 2 - len(tetromino.shape[0]) // 2, 0)
        return tetromino

    def start(self) -> None:
        """Start the game loop."""
        while not self.is_game_over:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self) -> None:
        """Handle user input events."""
        events = pygame.event.get()
        if not self.input_handler.process_events(
            events, self.current_tetromino, self.board
        ):
            self.is_game_over = True

    def update(self) -> None:
        """Update the game state."""
        current_time = pygame.time.get_ticks()
        # Adjust drop interval based on level (if desired)
        adjusted_drop_interval = max(
            100, self.drop_interval - (self.score_manager.level - 1) * 50
        )
        if current_time - self.last_drop_time > adjusted_drop_interval:
            new_position = Position(
                self.current_tetromino.position.x, self.current_tetromino.position.y + 1
            )
            if self.board.is_valid_position(self.current_tetromino, new_position):
                self.current_tetromino.move(0, 1)
            else:
                self.board.place_tetromino(self.current_tetromino)
                lines_cleared = self.board.clear_lines()
                if lines_cleared > 0:
                    self.score_manager.update_lines_cleared(lines_cleared)
                self.current_tetromino = self.get_new_tetromino()
                if not self.board.is_valid_position(
                    self.current_tetromino, self.current_tetromino.position
                ):
                    self.is_game_over = True
                    print("########################")
                    print("Game Over!")
                    print(f"Lines Cleared: {self.score_manager.lines_cleared}")
                    print("########################")

            self.last_drop_time = current_time

    def render(self) -> None:
        """Render the game state to the screen."""
        self.screen.fill(COLORS["BLACK"])
        self.renderer.draw_board(self.board)
        self.renderer.draw_tetromino(self.current_tetromino)
        self.renderer.draw_ui(self.score_manager)
        pygame.display.flip()
