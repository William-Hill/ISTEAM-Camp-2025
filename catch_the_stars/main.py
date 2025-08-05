"""
🎮 Catch the Stars - Enhanced Pygame Zero Game
A fun space-themed game for learning Python programming!

This game teaches:
- Basic game loops and event handling
- Sprite management and collision detection
- Sound effects and audio programming
- Score tracking and game state management
- Difficulty progression

Created for students aged 13-19 learning Python with AI assistance.
"""

import random

# ===== GAME SETTINGS =====
WIDTH = 800
HEIGHT = 600
TITLE = "Catch the Stars - Space Adventure!"

# ===== GAME VARIABLES =====
score = 0
lives = 3
level = 1
game_speed = 3
game_state = "playing"  # "playing", "game_over", "paused"

# ===== CREATE GAME OBJECTS =====
# Player spaceship
player = Actor("player")
player.pos = (WIDTH // 2, HEIGHT - 80)
player.speed = 5

# Star to catch
star = Actor("star")
star.pos = (random.randint(50, WIDTH - 50), -50)
star.speed = game_speed

# Background stars for visual effect
background_stars = []
for i in range(20):
    star_bg = Actor("star")
    star_bg.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    star_bg.speed = random.randint(1, 3)
    background_stars.append(star_bg)

# ===== SOUND EFFECTS =====
# Load sound effects (Pygame Zero automatically loads sounds from the sounds folder)
collect_sound = "collect"
miss_sound = "miss"
game_over_sound = "game_over"
background_music = "background_music"

# ===== GAME FUNCTIONS =====

def draw():
    """Draw everything on the screen - called every frame"""
    # Clear the screen and set background
    screen.clear()
    screen.fill((0, 0, 30))  # Dark blue space background
    
    # Draw background stars
    for star_bg in background_stars:
        star_bg.draw()
    
    # Draw main game objects
    player.draw()
    star.draw()
    
    # Draw UI elements
    draw_ui()
    
    # Draw game over screen if needed
    if game_state == "game_over":
        draw_game_over()

def draw_ui():
    """Draw the user interface (score, lives, level)"""
    # Score display
    screen.draw.text(f"Score: {score}", 
                    topleft=(20, 20), 
                    fontsize=40, 
                    color="white",
                    fontname="arial")
    
    # Lives display
    screen.draw.text(f"Lives: {'❤️' * lives}", 
                    topleft=(20, 70), 
                    fontsize=30, 
                    color="red",
                    fontname="arial")
    
    # Level display
    screen.draw.text(f"Level: {level}", 
                    topright=(WIDTH - 20, 20), 
                    fontsize=30, 
                    color="yellow",
                    fontname="arial")
    
    # Instructions
    screen.draw.text("Use ← → arrow keys to move", 
                    bottomleft=(20, HEIGHT - 20), 
                    fontsize=20, 
                    color="lightblue",
                    fontname="arial")

def draw_game_over():
    """Draw the game over screen"""
    # Semi-transparent overlay
    screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), (0, 0, 0, 128))
    
    # Game over text
    screen.draw.text("GAME OVER", 
                    center=(WIDTH // 2, HEIGHT // 2 - 50), 
                    fontsize=80, 
                    color="red",
                    fontname="arial")
    
    # Final score
    screen.draw.text(f"Final Score: {score}", 
                    center=(WIDTH // 2, HEIGHT // 2 + 20), 
                    fontsize=50, 
                    color="white",
                    fontname="arial")
    
    # Restart instructions
    screen.draw.text("Press SPACE to restart", 
                    center=(WIDTH // 2, HEIGHT // 2 + 80), 
                    fontsize=30, 
                    color="yellow",
                    fontname="arial")

def update():
    """Update game logic - called every frame"""
    global score, lives, level, game_speed, game_state
    
    # Only update if game is playing
    if game_state != "playing":
        return
    
    # ===== PLAYER MOVEMENT =====
    handle_player_movement()
    
    # ===== STAR MOVEMENT =====
    handle_star_movement()
    
    # ===== COLLISION DETECTION =====
    handle_collisions()
    
    # ===== BACKGROUND STARS =====
    update_background_stars()
    
    # ===== DIFFICULTY PROGRESSION =====
    check_level_progression()

def handle_player_movement():
    """Handle player spaceship movement"""
    # Get keyboard input
    if keyboard.left:
        player.x -= player.speed
    if keyboard.right:
        player.x += player.speed
    
    # Keep player on screen
    player.x = max(32, min(WIDTH - 32, player.x))

def handle_star_movement():
    """Handle star movement and resetting"""
    global lives, game_state
    
    # Move star down
    star.y += star.speed
    
    # Check if star was missed
    if star.y > HEIGHT + 50:
        lives -= 1
        sounds.play(miss_sound)
        
        if lives <= 0:
            game_over()
        else:
            reset_star()

def handle_collisions():
    """Handle collision between player and star"""
    global score
    
    # Check if player caught the star
    if player.colliderect(star):
        score += 10
        sounds.play(collect_sound)
        reset_star()

def update_background_stars():
    """Update background stars for visual effect"""
    for star_bg in background_stars:
        star_bg.y += star_bg.speed
        if star_bg.y > HEIGHT + 50:
            star_bg.y = -50
            star_bg.x = random.randint(0, WIDTH)

def check_level_progression():
    """Increase difficulty as score increases"""
    global level, game_speed
    
    new_level = (score // 100) + 1
    if new_level > level:
        level = new_level
        game_speed += 0.5
        star.speed = game_speed

def reset_star():
    """Reset star to top of screen with random position"""
    star.x = random.randint(50, WIDTH - 50)
    star.y = -50

def game_over():
    """Handle game over state"""
    global game_state
    game_state = "game_over"
    sounds.play(game_over_sound)

def reset_game():
    """Reset the game to start over"""
    global score, lives, level, game_speed, game_state
    
    score = 0
    lives = 3
    level = 1
    game_speed = 3
    game_state = "playing"
    
    # Reset player position
    player.pos = (WIDTH // 2, HEIGHT - 80)
    
    # Reset star
    reset_star()
    
    # Reset background stars
    for star_bg in background_stars:
        star_bg.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

def on_key_down(key):
    """Handle keyboard input"""
    global game_state
    
    # Restart game if game over
    if game_state == "game_over" and key == keys.SPACE:
        reset_game()
    
    # Pause/unpause game
    if key == keys.P:
        if game_state == "playing":
            game_state = "paused"
        elif game_state == "paused":
            game_state = "playing"

# ===== GAME STARTUP =====
# Start background music (optional - uncomment if you want music)
# music.play(background_music)

print("🚀 Catch the Stars game started!")
print("Controls:")
print("- Arrow keys: Move spaceship")
print("- P: Pause/Unpause")
print("- SPACE: Restart (when game over)")
print("Have fun catching stars! ✨") 