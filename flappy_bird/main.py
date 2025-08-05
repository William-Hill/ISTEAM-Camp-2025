# main.py
# Flappy Bird Clone using Pygame Zero + pgzhelper
# Run with: pgzrun main.py

import random
from pgzhelper import *  # Provides sprite animation & rotation helpers

# -----------------------------
# Game Settings
# -----------------------------
WIDTH = 400
HEIGHT = 708

GRAVITY = 0.3
GAP = 150           # Gap between top and bottom pipes
PIPE_SPEED = 2
SPAWN_INTERVAL = 1.5 # Seconds between pipe spawns

# -----------------------------
# Game State
# -----------------------------
bird = Actor("bird0", (75, 350))
bird.images = ["bird0", "bird1", "bird2"]  # Flapping animation frames
bird.fps = 10
bird.vy = 0

pipes = []      # Holds tuples of (top_pipe, bottom_pipe)
score = 0
game_over = False

# -----------------------------
# Functions
# -----------------------------
def create_pipe():
    """Create a new pair of pipes with a random gap position."""
    gap_y = random.randint(150, 500)
    top_pipe = Actor("top", (WIDTH + 50, gap_y - GAP // 2 - 320))      # Adjust for pipe image height (~640px)
    bottom_pipe = Actor("bottom", (WIDTH + 50, gap_y + GAP // 2 + 320))
    pipes.append((top_pipe, bottom_pipe))

def reset_game():
    """Reset the game state to start a new round."""
    global pipes, score, game_over
    bird.y = 350
    bird.vy = 0
    bird.angle = 0
    pipes = []
    score = 0
    game_over = False

def draw():
    """Draw all game objects."""
    screen.blit("background", (0, 0))

    for top, bottom in pipes:
        top.draw()
        bottom.draw()

    bird.draw()

    # Score
    screen.draw.text(f"Score: {score}", midtop=(WIDTH//2, 10), fontsize=40, color="white")

    # Game Over message
    if game_over:
        screen.draw.text("GAME OVER!", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text("Press SPACE to restart", center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="yellow")

def update():
    """Update game logic each frame."""
    global game_over, score

    if game_over:
        return

    # Bird gravity and animation
    bird.vy += GRAVITY
    bird.y += bird.vy
    bird.next_image()  # Animate flapping
    bird.angle = max(-30, min(60, -bird.vy * 5))  # Tilt up when flapping, down when falling

    # Move pipes
    for top, bottom in pipes:
        top.x -= PIPE_SPEED
        bottom.x -= PIPE_SPEED

    # Remove passed pipes and increment score
    if pipes and pipes[0][0].right < 0:
        pipes.pop(0)
        score += 1

    # Collision detection with pipes or screen bounds
    for top, bottom in pipes:
        if bird.colliderect(top) or bird.colliderect(bottom) or bird.top < 0 or bird.bottom > HEIGHT:
            game_over = True
            break

def on_key_down(key):
    """Handle key presses for flap and restart."""
    global game_over
    if key == keys.SPACE:
        if game_over:
            reset_game()
        else:
            bird.vy = -6  # Flap upward

def update_pipes():
    """Spawn pipes periodically."""
    if not game_over and (not pipes or pipes[-1][0].x < WIDTH - 200):
        create_pipe()

# Schedule pipe spawning
clock.schedule_interval(update_pipes, SPAWN_INTERVAL)
