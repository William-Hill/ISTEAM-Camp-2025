# 🎮 Pygame Zero Example Game: *Catch the Stars*

This README will guide you through creating a simple 2D game using **Pygame Zero**.  
In this game, the player moves a character left and right to catch falling stars for points.

---

## 1️⃣ Install Requirements

Ensure you have **Python 3.9+** installed. Then install Pygame Zero:

```bash
pip install pgzero
```

Check that it works:

```bash
pgzrun --version
```

---

## 2️⃣ Project Structure

```
catch_the_stars/
├── main.py        # Game code
├── images/
│   ├── player.png # 64x64 image of your player
│   └── star.png   # 32x32 image of a star
```

> **Note:** Place your images in the `images` folder.  
> Pygame Zero automatically loads images by filename.

---

## 3️⃣ Example Game Code (`main.py`)

```python
import random

# Screen size
WIDTH = 800
HEIGHT = 600

# Load actors
player = Actor("player")
player.pos = (WIDTH // 2, HEIGHT - 50)

star = Actor("star")
star.pos = (random.randint(0, WIDTH), 0)

score = 0
speed = 4

def draw():
    screen.clear()
    screen.fill((0, 0, 30))  # Dark blue background
    player.draw()
    star.draw()
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=40, color="white")

def update():
    global score, speed

    # Player movement
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5

    # Keep player on screen
    player.x = max(0, min(WIDTH, player.x))

    # Move the star
    star.y += speed

    # Check for catching the star
    if player.colliderect(star):
        score += 1
        reset_star()

    # Reset star if missed
    if star.y > HEIGHT:
        reset_star()

def reset_star():
    global speed
    star.x = random.randint(0, WIDTH)
    star.y = 0
    speed += 0.2  # Gradually increase difficulty
```

---

## 4️⃣ Run the Game

In the project folder, run:

```bash
pgzrun main.py
```

Use the **arrow keys** to move and catch stars!

---

## 5️⃣ Next Steps / Challenges

- Add **more stars** that fall at different speeds.
- Add **sound effects** when a star is caught or missed.
- Create **game over logic** after missing 3 stars.
- Replace the player with a custom sprite you design in **Piskel**.
