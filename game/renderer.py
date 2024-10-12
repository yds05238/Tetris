# game/renderer.py

import pygame
from typing import Any
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, COLORS
from game.board import Board
from game.tetromino import Tetromino
from score_manager import ScoreManager
from game.enums import Color


class Renderer:
    """Class responsible for rendering game elements using Pygame."""

    def __init__(self, screen: Any):
        """
        Initialize the renderer.
        Args:
            screen (Any): The Pygame screen surface.
        """
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 18)

    def draw_board(self, board: Board) -> None:
        """Draw the game board.

        Args:
            board (Board): The game board.
        """
        for y in range(board.height):
            for x in range(board.width):
                cell_color = COLORS[board.grid[y][x].value]
                pygame.draw.rect(
                    self.screen,
                    cell_color,
                    pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                )
                # Draw grid lines
                pygame.draw.rect(
                    self.screen,
                    COLORS["GRAY"],
                    pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    1,  # Border width
                )

    def draw_tetromino(self, tetromino: Tetromino) -> None:
        """Draw the current tetromino.

        Args:
            tetromino (Tetromino): The tetromino to draw.
        """
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = tetromino.position.x + x
                    grid_y = tetromino.position.y + y
                    if grid_y >= 0:
                        cell_color = COLORS[tetromino.color.value]
                        pygame.draw.rect(
                            self.screen,
                            cell_color,
                            pygame.Rect(
                                grid_x * CELL_SIZE,
                                grid_y * CELL_SIZE,
                                CELL_SIZE,
                                CELL_SIZE,
                            ),
                        )
                        # Draw grid lines
                        pygame.draw.rect(
                            self.screen,
                            COLORS["GRAY"],
                            pygame.Rect(
                                grid_x * CELL_SIZE,
                                grid_y * CELL_SIZE,
                                CELL_SIZE,
                                CELL_SIZE,
                            ),
                            1,  # Border width
                        )

    def draw_ui(self, score_manager: ScoreManager) -> None:
        """Draw UI elements like score and level.

        Args:
            score_manager (ScoreManager): The score manager.
        """
        score_text = self.font.render(
            f"Score: {score_manager.score}", True, COLORS["WHITE"]
        )
        level_text = self.font.render(
            f"Level: {score_manager.level}", True, COLORS["WHITE"]
        )
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 30))
