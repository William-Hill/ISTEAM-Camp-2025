# 🎮 Catch the Stars - Pygame Zero Learning Game

A fun space-themed game created to teach Python programming concepts to students aged 13-19 using Pygame Zero and AI assistance.

## 🚀 What You'll Learn

This project teaches fundamental programming concepts through game development:

- **Game Loops & Event Handling**: Understanding how games run continuously
- **Sprite Management**: Working with images and game objects
- **Collision Detection**: Detecting when objects touch each other
- **Sound Programming**: Adding audio effects to your game
- **State Management**: Handling different game states (playing, paused, game over)
- **Score Tracking**: Managing and displaying game statistics
- **Difficulty Progression**: Making games more challenging over time

## 📁 Project Structure

```
catch_the_stars/
├── main.py              # Main game code
├── create_sprites.py    # Script to generate placeholder sprites
├── create_sounds.py     # Script to generate placeholder sounds
├── images/
│   ├── player.png       # Player spaceship sprite
│   ├── star.png         # Star sprite to catch
│   └── background.png   # Space background
├── sounds/
│   ├── collect.wav      # Sound when catching a star
│   ├── miss.wav         # Sound when missing a star
│   ├── game_over.wav    # Game over sound
│   └── background_music.wav # Background music
└── README.md           # This file
```

## 🛠️ Setup Instructions

### 1. Install Python and Pygame Zero

Make sure you have Python 3.9+ installed, then install Pygame Zero:

```bash
pip install pgzero
```

### 2. Generate Game Assets

Run these commands to create the placeholder sprites and sounds:

```bash
python3 create_sprites.py
python3 create_sounds.py
```

### 3. Run the Game

```bash
pgzrun main.py
```

## 🎯 How to Play

- **Move**: Use the left and right arrow keys to move your spaceship
- **Goal**: Catch the falling stars to earn points
- **Lives**: You have 3 lives - miss a star and you lose a life
- **Levels**: The game gets faster as your score increases
- **Pause**: Press 'P' to pause/unpause the game
- **Restart**: Press SPACE when game over to play again

## 🎨 Customizing Your Game

### Replacing Sprites

1. **Find or create your own images** (PNG format recommended)
2. **Replace the files in the `images/` folder**:
   - `player.png` - Your spaceship/character (64x64 pixels works well)
   - `star.png` - The object to catch (32x32 pixels works well)
   - `background.png` - Background image (800x600 pixels)

### Replacing Sounds

1. **Find or create your own sound effects** (WAV format recommended)
2. **Replace the files in the `sounds/` folder**:
   - `collect.wav` - Happy sound for catching stars
   - `miss.wav` - Sad sound for missing stars
   - `game_over.wav` - Sound for when game ends
   - `background_music.wav` - Background music (optional)

### Modifying Game Code

The `main.py` file is heavily commented to help you understand each part:

- **Game Settings**: Change screen size, title, and initial values
- **Game Objects**: Modify player speed, star behavior, etc.
- **Scoring**: Adjust points per star, lives, difficulty progression
- **Visual Effects**: Add particles, animations, or new UI elements

## 🧠 Learning Challenges

Try these modifications to learn more:

### Beginner Challenges
1. **Change the colors**: Modify the background color or sprite colors
2. **Adjust difficulty**: Change the star speed or player movement speed
3. **Add a high score**: Save the best score to a file

### Intermediate Challenges
1. **Multiple stars**: Make multiple stars fall at once
2. **Power-ups**: Add special stars that give bonus points or extra lives
3. **Different star types**: Create stars worth different point values
4. **Particle effects**: Add sparkles when catching stars

### Advanced Challenges
1. **Enemy objects**: Add objects that hurt the player if touched
2. **Shooting mechanics**: Let the player shoot at enemies
3. **Level system**: Create different levels with unique challenges
4. **Save/load system**: Save game progress between sessions

## 🤖 AI-Assisted Learning

This project is designed to work with AI coding assistants like:

- **GitHub Copilot**: Get code suggestions as you type
- **ChatGPT**: Ask questions about the code or get help with modifications
- **Claude**: Get explanations of complex programming concepts

### Example AI Prompts

- "How do I add a power-up that gives the player extra speed?"
- "Can you explain how the collision detection works in this game?"
- "I want to add a boss battle at the end of each level. How would I do that?"
- "How can I make the background stars twinkle?"

## 🔧 Troubleshooting

### Common Issues

1. **"pgzrun command not found"**
   - Make sure you installed pgzero: `pip install pgzero`
   - Try: `python -m pgzero main.py`

2. **"Image not found" errors**
   - Check that your image files are in the `images/` folder
   - Make sure the filenames match exactly (case-sensitive)

3. **"Sound not found" errors**
   - Check that your sound files are in the `sounds/` folder
   - Make sure the filenames match exactly (case-sensitive)

4. **Game runs slowly**
   - Try reducing the number of background stars
   - Check if your computer meets the minimum requirements

### Getting Help

- Check the [Pygame Zero documentation](https://pygame-zero.readthedocs.io/)
- Ask questions in programming forums or Discord servers
- Use AI assistants to help debug issues

## 📚 Additional Resources

- **Pygame Zero Documentation**: https://pygame-zero.readthedocs.io/
- **Python Game Development**: https://realpython.com/pygame-a-primer/
- **Free Game Assets**: 
  - [Kenney.nl](https://kenney.nl/) - Free game art and sounds
  - [OpenGameArt.org](https://opengameart.org/) - Community game assets
  - [Freesound.org](https://freesound.org/) - Free sound effects

## 🎓 Educational Standards

This project aligns with computer science learning objectives:

- **Computational Thinking**: Problem decomposition, pattern recognition
- **Programming Concepts**: Variables, functions, loops, conditionals
- **Game Design**: User experience, difficulty balancing, feedback systems
- **Digital Media**: Working with images, audio, and interactive content

## 🤝 Contributing

Feel free to:
- Share your modified versions of the game
- Suggest improvements or new features
- Create tutorials or learning materials
- Help other students learn programming

## 📄 License

This project is open source and available for educational use. The placeholder assets are generated programmatically and are free to use and modify.

---

**Happy coding! 🚀✨**

*Remember: The best way to learn programming is by doing. Don't be afraid to experiment, make mistakes, and ask for help!* 