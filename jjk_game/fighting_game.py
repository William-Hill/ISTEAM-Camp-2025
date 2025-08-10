import pgzrun
from pgzhelper import *

# Game setup
WIDTH = 1200
HEIGHT = 600
TITLE = "JJK vs Solo Leveling: Fighting Game"

# Player class for both characters
class Fighter:
    def __init__(self, name, x, y, is_player_one=True):
        self.name = name
        self.is_player_one = is_player_one
        
        # Load animations based on character
        if name == "Gojo":
            self.load_gojo_animations()
        else:  # Jin-Woo
            self.load_jinwoo_animations()
        
        # Create actor
        self.actor = Actor(self.stand_frames[0], (x, y))
        self.actor.scale = 2
        
        # Animation state
        self.current_animation = "stand"
        self.animation_frame = 0
        self.animation_speed = 0.2
        self.animation_timer = 0
        
        # Movement
        self.speed = 4
        self.direction = 1 if is_player_one else -1  # 1 for right, -1 for left
        self.actor.flip_x = not is_player_one  # Flip Jin-Woo to face Gojo
        
        # Jump state
        self.is_jumping = False
        self.jump_velocity = 0
        self.jump_speed = -15
        self.gravity = 0.8
        self.ground_y = HEIGHT - 150  # Ground level
        
        # Attack state
        self.is_attacking = False
        self.attack_timer = 0
        self.attack_duration = 30
        self.current_attack_type = None
        
        # Health
        self.health = 100
        self.max_health = 100
        
    def load_gojo_animations(self):
        # Load Gojo animation frames
        self.stand_frames = []
        for i in range(1, 5):
            self.stand_frames.append(f"gojo-stand_{i}")
        
        self.walk_frames = []
        for i in range(1, 9):
            self.walk_frames.append(f"gojo-walk_{i}")
        
        self.jump_frames = []
        for i in range(1, 5):
            self.jump_frames.append(f"jump_{i}")
        
        self.light_attack_frames = []
        for i in range(1, 7):
            self.light_attack_frames.append(f"light_attack_{i}")
        
        self.heavy_attack_frames = []
        for i in range(1, 6):
            self.heavy_attack_frames.append(f"heavy_attack_{i}")
    
    def load_jinwoo_animations(self):
        # Load Jin-Woo animation frames
        self.stand_frames = []
        for i in range(1, 5):
            self.stand_frames.append(f"jinwoo_stand_{i}")
        
        self.walk_frames = []
        for i in range(1, 9):
            self.walk_frames.append(f"run_{i}")
        
        self.jump_frames = []
        for i in range(1, 5):
            self.jump_frames.append(f"jinwoo_jump_{i}")
        
        self.light_attack_frames = []
        for i in range(1, 7):
            self.light_attack_frames.append(f"jinwoo_light_attack_{i}")
        
        self.heavy_attack_frames = []
        for i in range(1, 7):
            self.heavy_attack_frames.append(f"jinwoo-heavy-attack{i}")
    
    def update(self, opponent):
        # Handle input based on player
        if self.is_player_one:
            self.handle_player_one_input()
        else:
            self.handle_player_two_input()
        
        # Handle attack timer
        if self.is_attacking:
            self.attack_timer += 1
            if self.attack_timer >= self.attack_duration:
                self.is_attacking = False
                self.attack_timer = 0
                self.current_attack_type = None
                self.current_animation = "stand"
        
        # Handle jumping physics
        if self.is_jumping:
            self.actor.y += self.jump_velocity
            self.jump_velocity += self.gravity
            
            # Check if landed
            if self.actor.y >= self.ground_y:
                self.actor.y = self.ground_y
                self.is_jumping = False
                self.jump_velocity = 0
                self.current_animation = "stand"
        
        # Set animation based on state
        if self.is_attacking:
            if self.current_attack_type == "heavy":
                self.current_animation = "heavy_attack"
            else:
                self.current_animation = "light_attack"
        elif self.is_jumping:
            self.current_animation = "jump"
        elif self.current_animation == "walk":
            pass  # Keep walk animation
        else:
            self.current_animation = "stand"
        
        # Keep player on screen
        if self.is_player_one:
            self.actor.x = max(100, min(WIDTH//2 - 50, self.actor.x))
        else:
            self.actor.x = max(WIDTH//2 + 50, min(WIDTH - 100, self.actor.x))
        
        # Update animation
        frames = self.get_current_frames()
        
        if self.current_animation == "jump":
            # For jump, cycle through frames based on jump progress
            if self.is_jumping:
                jump_progress = (self.jump_velocity - self.jump_speed) / (0 - self.jump_speed)
                self.animation_frame = min(3, int(jump_progress * 4))
            else:
                self.animation_frame = 0
        elif self.current_animation == "light_attack":
            # For light attack, cycle through frames based on attack timer
            if self.is_attacking:
                attack_progress = self.attack_timer / self.attack_duration
                self.animation_frame = min(5, int(attack_progress * 6))
            else:
                self.animation_frame = 0
        elif self.current_animation == "heavy_attack":
            # For heavy attack, cycle through frames based on attack timer
            if self.is_attacking:
                attack_progress = self.attack_timer / self.attack_duration
                self.animation_frame = min(4, int(attack_progress * 5))
            else:
                self.animation_frame = 0
        else:
            # Normal animation cycling for stand and walk
            self.animation_timer += self.animation_speed
            if self.animation_timer >= 1:
                self.animation_timer = 0
                self.animation_frame = (self.animation_frame + 1) % len(frames)
        
        # Set current frame with bounds checking
        if 0 <= self.animation_frame < len(frames):
            self.actor.image = frames[self.animation_frame]
            self.actor.scale = 2
    
    def handle_player_one_input(self):
        # Player 1 controls (WASD + J/K)
        if keyboard.j and not self.is_attacking and not self.is_jumping:
            self.is_attacking = True
            self.attack_timer = 0
            self.current_attack_type = "light"
        
        if keyboard.k and not self.is_attacking and not self.is_jumping:
            self.is_attacking = True
            self.attack_timer = 0
            self.current_attack_type = "heavy"
        
        if (keyboard.w or keyboard.space) and not self.is_jumping and not self.is_attacking:
            self.is_jumping = True
            self.jump_velocity = self.jump_speed
            self.current_animation = "jump"
        
        if keyboard.a:
            self.actor.x -= self.speed
            self.direction = -1
            self.actor.flip_x = True
            self.current_animation = "walk"
        elif keyboard.d:
            self.actor.x += self.speed
            self.direction = 1
            self.actor.flip_x = False
            self.current_animation = "walk"
        else:
            self.current_animation = "stand"
    
    def handle_player_two_input(self):
        # Player 2 controls (Arrow Keys + N/M)
        if keyboard.n and not self.is_attacking and not self.is_jumping:
            self.is_attacking = True
            self.attack_timer = 0
            self.current_attack_type = "light"
        
        if keyboard.m and not self.is_attacking and not self.is_jumping:
            self.is_attacking = True
            self.attack_timer = 0
            self.current_attack_type = "heavy"
        
        if keyboard.up and not self.is_jumping and not self.is_attacking:
            self.is_jumping = True
            self.jump_velocity = self.jump_speed
            self.current_animation = "jump"
        
        if keyboard.left:
            self.actor.x -= self.speed
            self.direction = -1
            self.actor.flip_x = True
            self.current_animation = "walk"
        elif keyboard.right:
            self.actor.x += self.speed
            self.direction = 1
            self.actor.flip_x = False
            self.current_animation = "walk"
        else:
            self.current_animation = "stand"
    
    def get_current_frames(self):
        if self.current_animation == "walk":
            return self.walk_frames
        elif self.current_animation == "jump":
            return self.jump_frames
        elif self.current_animation == "light_attack":
            return self.light_attack_frames
        elif self.current_animation == "heavy_attack":
            return self.heavy_attack_frames
        else:
            return self.stand_frames
    
    def draw(self):
        self.actor.draw()
        
        # Draw health bar
        bar_width = 200
        bar_height = 20
        x = 50 if self.is_player_one else WIDTH - 250
        y = 50
        
        # Background
        screen.draw.filled_rect(Rect(x, y, bar_width, bar_height), (100, 100, 100))
        # Health
        health_width = (self.health / self.max_health) * bar_width
        screen.draw.filled_rect(Rect(x, y, health_width, bar_height), (255, 0, 0))
        # Border
        screen.draw.rect(Rect(x, y, bar_width, bar_height), (255, 255, 255))
        
        # Name
        screen.draw.text(self.name, (x, y - 25), color="white", fontsize=16)

# Create fighters
gojo = Fighter("Gojo", 200, HEIGHT - 150, True)
jinwoo = Fighter("Jin-Woo", WIDTH - 200, HEIGHT - 150, False)

def update():
    gojo.update(jinwoo)
    jinwoo.update(gojo)

def draw():
    screen.fill((50, 100, 150))  # Dark blue background
    
    # Draw ground
    screen.draw.filled_rect(Rect(0, HEIGHT - 100, WIDTH, 100), (100, 150, 100))
    
    # Draw center line
    screen.draw.line((WIDTH//2, HEIGHT - 100), (WIDTH//2, HEIGHT), (255, 255, 255))
    
    # Draw fighters
    gojo.draw()
    jinwoo.draw()
    
    # Draw instructions
    screen.draw.text("Player 1 (Gojo): WASD to move, W/Space to jump, J=Light, K=Heavy", (10, HEIGHT - 30), color="white", fontsize=16)
    screen.draw.text("Player 2 (Jin-Woo): Arrow Keys to move, Up to jump, N=Light, M=Heavy", (WIDTH - 400, HEIGHT - 30), color="white", fontsize=16)
    
    screen.draw.text("JJK vs Solo Leveling: Fighting Game", (WIDTH//2 - 150, 10), color="white", fontsize=24)

pgzrun.go() 