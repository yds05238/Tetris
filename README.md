# Tetris

Tetris


## Overview of the Game Components

- Game Loop: Controls the game flow
- Board/Grid: The playing field where tetrominoes fall
- Tetrominoes: Tehe shapes made up of blocks
- Blocks: individual elements of the tetrominoes
- Input Handling: Captures player inputs
- Rendering: Draws game elements on the screen
- Collision Detection: Determines interactions between tetrominoes and the board
- Scoring and Levels: manages player's score and game difficulty
- Game State Management: Handles different game states (playing, paused, game over)

## Proposed Classes and Interfaces

- Game Class
  - Acts as the controller of the game. Manages the game loop, innitializes other components, and handles the game state.
  - Key Methods
    - run(): starts the game loop
    - handle_events(): handles player inputs
    - update(): updates the game logic
    - draw(): renders the game state
- Board Class
  - Represnts the game board/grid. Manages the placement of tetrominoes and cleared lines
  - Key Attributes
    - grid: 2D array representing the board state
  - Key Methods
    - add_tetromino(tetromino): places a tetromino onto the board
    - clear_lines(): removes full rows from the board
    - is_valid_position(tetromino, position): checks if a tetromino can be placed at a position
- Tetromino Class
  - Represents a tetromino shape and its rotation state
  - Key Attributes
    - shape: the shape of the tetromino
    - color: the color of the tetromino
    - position: the current position of the tetromino on the board
  - Key Methods
    - rotate(): rotates the tetromino to the next rotation state
    - move(direction): moves the tetrmino left, right, or down
    - Subclasses
      - TetrominoI, TetrominoJ, TetrominoL, TetrominoO, TetrominoS, TetrominoT, TetrominoZ
      - Each sub class defines the specific shape attribute
- TetrominoFactory Class
  - Generates random tetrominoes
  - Key Methods
    - get_tetromino(): returns a randomly selected tetromino
- InputHandler Class
  - Handles user inputs an dmaps them to game actions
  - Key Methods
    - handle_input(event): handles a single input event
- Renderer Class
  - Handles all drawing operations
  - Key Methods
    - draw_board(board): renders the board on the screen
    - draw_tetromino(tetromino): renders a tetromino on the screen
    - draw_next_tetromino(tetromino): renders the upcoming tetromino on the screen
    - draw_ui(): Draws the score, level, and other UI elements
- CollisionManager Class
  - Detects collision between tetrominoes and the board boundaries or other tetrominoes
  - Key Methods
    - check_collision(tetromino, board): checks if a tetromino has collided with the board or other tetrominoes
- ScoreManager Class
  - Manages the player's score and level progression
  - Key Attributes
    - score: the current score
    - level: the current level
    - lines_cleared: the number of lines cleared
  - Key Methods
    - update_score(lines): updates the score based on the number of lines cleared
    - update_level(): updates the level based on the number of lines cleared
- SoundManager Class
  - Manages game sounds and music
  - Key Methods
    - play_sound(effect): plays a sound effect
    - play_music(track): plays the background music
    - stop_music(): stops the background music
- Constants Module
  - Stores constant values used across the game (e.g. colors, screen dimensions, etc)
  - Usage: Import constants wherever needed to avoid magic numbers
