# 🎮 iTeam Demo - Python Game Collection

A collection of educational Python games built with **Pygame Zero** for learning game development and programming concepts.

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+** installed
- Virtual environment (recommended)

### Setup
1. **Clone and navigate to the project:**
   ```bash
   cd isteam-demo
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install pgzero pgzhelper
   ```

4. **Run any game:**
   ```bash
   pgzrun game_directory/main.py
   ```

---

## 🎯 Games Overview

### 1. 🛸 **Catch the Stars** (`catch_the_stars/`)
**Space-themed arcade game** - Control a spaceship to catch falling stars!

**🎮 How to Play:**
- Use **LEFT/RIGHT arrow keys** to move your spaceship
- Catch falling stars to earn points
- Avoid missing stars - you have 3 lives
- Game gets faster as you progress through levels

**📚 Learning Concepts:**
- Basic game loops and event handling
- Sprite management and collision detection
- Sound effects and audio programming
- Score tracking and game state management
- Difficulty progression and level systems

**🎵 Features:**
- Background music and sound effects
- Animated background stars
- Lives system with heart display
- Level progression with increasing speed
- Game over screen with restart option

**🚀 Run it:**
```bash
cd catch_the_stars
pgzrun main.py
```

---

### 2. 🐦 **Flappy Bird** (`flappy_bird/`)
**Classic Flappy Bird clone** - Guide the bird through pipes!

**🎮 How to Play:**
- Press **SPACEBAR** to make the bird flap
- Navigate through gaps in the pipes
- Don't hit the pipes or the ground/ceiling
- Try to get the highest score possible

**📚 Learning Concepts:**
- Physics simulation (gravity, velocity)
- Sprite animation and rotation
- Procedural level generation
- Collision detection with multiple objects
- Game restart mechanics

**🎵 Features:**
- Smooth bird animation (3-frame flapping)
- Dynamic bird rotation based on velocity
- Procedurally generated pipes with random gaps
- Score tracking
- Game over screen with restart option

**🚀 Run it:**
```bash
cd flappy_bird
pgzrun main.py
```

---

### 3. 👽 **Pygame Zero Intro** (`pygame_zero_intro/`)
**Beginner-friendly tutorial game** - Learn Pygame Zero basics!

**🎮 How to Play:**
- Watch the alien move across the screen
- **Click on the alien** to make it hurt
- Listen for sound effects
- Learn basic Pygame Zero concepts

**📚 Learning Concepts:**
- Creating a game window and drawing backgrounds
- Loading and displaying sprites
- Moving sprites with the update() function
- Handling mouse clicks and collision detection
- Playing sounds and changing sprite images
- Using the clock for timed events

**🎵 Features:**
- Simple alien sprite that moves automatically
- Click interaction with visual feedback
- Sound effects on interaction
- Sprite image switching (normal/hurt states)
- Perfect for absolute beginners

**🚀 Run it:**
```bash
cd pygame_zero_intro
pgzrun intro.py
```

---

## 📁 Project Structure

```
isteam-demo/
├── catch_the_stars/          # Space arcade game
│   ├── main.py              # Main game code
│   ├── requirements.txt     # Dependencies
│   ├── images/              # Game sprites
│   │   ├── player.png       # Spaceship sprite
│   │   ├── star.png         # Star sprite
│   │   └── background.png   # Background image
│   ├── sounds/              # Audio files
│   │   ├── collect.wav      # Star collection sound
│   │   ├── miss.wav         # Miss sound
│   │   ├── game_over.wav    # Game over sound
│   │   └── background_music.wav
│   ├── README.md            # Game-specific documentation
│   ├── TEACHER_GUIDE.md     # Educational guide
│   └── setup.py             # Installation script
├── flappy_bird/             # Flappy Bird clone
│   ├── main.py              # Main game code
│   └── images/              # Game sprites
│       ├── bird0.png        # Bird animation frames
│       ├── bird1.png
│       ├── bird2.png
│       ├── top.png          # Pipe sprites
│       ├── bottom.png
│       └── background.png
├── pygame_zero_intro/       # Beginner tutorial
│   ├── intro.py             # Main game code
│   ├── images/              # Game sprites
│   │   ├── alien.png        # Normal alien
│   │   └── alien_hurt.png   # Hurt alien
│   ├── sounds/              # Audio files
│   │   └── eep.wav          # Hurt sound
│   └── README.md            # Tutorial documentation
├── venv/                    # Virtual environment
├── .gitignore              # Git ignore file
└── README.md               # This file
```

---

## 🛠️ Development

### Adding New Games
1. Create a new directory for your game
2. Include a `main.py` file with your game code
3. Add `images/` and `sounds/` folders as needed
4. Update this README with game information

### Dependencies
- **pgzero**: Main game framework
- **pgzhelper**: Enhanced sprite and collision utilities
- **Pillow**: Image processing (for some games)

### Running Games
All games use the same command pattern:
```bash
pgzrun game_directory/main.py
```

---

## 🎓 Educational Value

These games are designed to teach:
- **Programming fundamentals** through game development
- **Object-oriented programming** concepts
- **Event-driven programming** and user input
- **Game design principles** and mechanics
- **Problem-solving** and debugging skills

Perfect for:
- Students learning Python (ages 13-19)
- Programming workshops and coding clubs
- Self-directed learning projects
- Computer science education

---

## 🤝 Contributing

Feel free to:
- Add new games to the collection
- Improve existing games
- Add educational documentation
- Create tutorials or guides

---

## 📄 License

This project is open source and available under the MIT License.

---

**Happy coding! 🎮✨**
