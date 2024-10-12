import pygame
from board import Board
from input_handler import InputHandler
from renderer import Renderer
from tetromino_factory import TetrominoFactory
from collision_manager import CollisionManager
from score_manager import ScoreManager
import constants


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.input_handler = InputHandler()
        self.renderer = Renderer(self.screen)
        self.tetromino_factory = TetrominoFactory()
        self.collision_manager = CollisionManager(self.board)
        self.score_manager = ScoreManager()
        self.current_tetromino = self.tetromino_factory.get_random_tetromino()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # Limit to 60 FPS

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
        self.input_handler.process_input(
            events, self.current_tetromino, self.collision_manager
        )

    def update(self):
        # Update game logic
        pass

    def draw(self):
        self.renderer.draw_board(self.board)
        self.renderer.draw_tetromino(self.current_tetromino)
        pygame.display.flip()
