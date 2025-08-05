"""
🎮 Pygame Zero Introduction Tutorial Game
Based on the official Pygame Zero documentation tutorial

This game demonstrates:
- Creating a window and drawing a background
- Loading and displaying sprites
- Moving sprites with the update() function
- Handling mouse clicks and collision detection
- Playing sounds and changing sprite images
- Using the clock for timed events

Perfect for beginners learning Python game development!
"""

# ===== WINDOW SETUP =====
WIDTH = 500
HEIGHT = 300

# ===== SPRITE SETUP =====
# Create an alien actor - Pygame Zero will look for 'alien.png' in the images folder
alien = Actor('alien')
alien.pos = 100, 56

# ===== GAME FUNCTIONS =====

def draw():
    """Draw everything on the screen - called every frame"""
    # Clear the screen and fill with a reddish background
    screen.fill((128, 0, 0))  # Medium-dark red
    # Draw the alien sprite
    alien.draw()

def update():
    """Update game logic - called every frame"""
    # Move the alien to the right
    alien.left += 2
    
    # If alien goes off the right side, reset to the left
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    """Handle mouse clicks"""
    # Check if the click was on the alien
    if alien.collidepoint(pos):
        # Clicked on alien - make it hurt!
        set_alien_hurt()
    else:
        # Missed the alien
        print("You missed me!")

def set_alien_hurt():
    """Make the alien look hurt and play sound"""
    alien.image = 'alien_hurt'  # Change to hurt sprite
    sounds.eep.play()  # Play hurt sound
    # Schedule the alien to return to normal after 1 second
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    """Return the alien to normal appearance"""
    alien.image = 'alien'  # Change back to normal sprite

# ===== GAME STARTUP =====
print("👽 Alien Game Started!")
print("Click on the alien to make it hurt!")
print("Watch it move across the screen!")
print("Press Ctrl-Q (or Cmd-Q on Mac) to quit") 