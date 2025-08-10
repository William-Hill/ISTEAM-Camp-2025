# JJK: Gojo's Adventure

A simple 2D platformer game featuring Gojo Satoru from Jujutsu Kaisen, built with Pygame Zero.

## Features

- **Animated Character**: Gojo with stand and walk animations
- **Smooth Movement**: Use A/D or Arrow keys to move
- **Sprite Flipping**: Character automatically faces the direction of movement
- **Transparent Sprites**: Clean character sprites with transparent backgrounds

## Controls

- **A** or **Left Arrow**: Move left
- **D** or **Right Arrow**: Move right
- **No key pressed**: Stand idle

## How to Run

1. Make sure you have the required dependencies installed:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Run the game:
   ```bash
   pgzrun main.py
   ```

## Game Structure

- `main.py` - Main game file with player logic and rendering
- `images/` - Contains all the Gojo sprite frames
  - `gojo-stand_1.png` to `gojo-stand_4.png` - Standing animation frames
  - `gojo-walk_1.png` to `gojo-walk_8.png` - Walking animation frames

## Technical Details

- **Engine**: Pygame Zero
- **Sprite Dimensions**: 
  - Stand frames: 33x68 pixels
  - Walk frames: 35x68 pixels
- **Animation Speed**: 0.2 (adjustable in the Player class)
- **Movement Speed**: 3 pixels per frame

## Future Enhancements

- Add jumping mechanics
- Include enemies and combat
- Add different levels/backgrounds
- Implement special abilities (Infinity, Blue, Red, Purple)
- Add sound effects and music 