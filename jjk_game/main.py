import pgzrun
from pgzhelper import *

# Game setup
WIDTH = 800
HEIGHT = 600
TITLE = "JJK: Gojo's Adventure"

# Player class
class Player:
    def __init__(self):
        # Load stand animation frames
        self.stand_frames = []
        for i in range(1, 5):  # 4 stand frames
            self.stand_frames.append(f"gojo-stand_{i}")
        
        # Load walk animation frames
        self.walk_frames = []
        for i in range(1, 9):  # 8 walk frames
            self.walk_frames.append(f"gojo-walk_{i}")
        
        # Load crouch animation frames
        self.crouch_frames = []
        for i in range(1, 5):  # 4 crouch frames
            self.crouch_frames.append(f"gojo-crouch_{i}")
        
        # Load jump animation frames
        self.jump_frames = []
        for i in range(1, 5):  # 4 jump frames
            self.jump_frames.append(f"jump_{i}")
        
        # Load light attack animation frames
        self.light_attack_frames = []
        for i in range(1, 7):  # 6 light attack frames
            self.light_attack_frames.append(f"light_attack_{i}")
        
        # Load heavy attack animation frames
        self.heavy_attack_frames = []
        for i in range(1, 6):  # 5 heavy attack frames
            self.heavy_attack_frames.append(f"heavy_attack_{i}")
        

        
        # Create player actor
        self.actor = Actor(self.stand_frames[0], (WIDTH//2, HEIGHT//2))  # Use first stand frame
        self.actor.scale = 2  # Make sprite bigger
        
        # Animation state
        self.current_animation = "stance-2_1"
        self.animation_frame = 0
        self.animation_speed = 0.2
        self.animation_timer = 0
        
        # Movement
        self.speed = 3
        self.direction = 1  # 1 for right, -1 for left
        
        # Crouch state
        self.is_crouching = False
        
        # Jump state
        self.is_jumping = False
        self.jump_velocity = 0
        self.jump_speed = -15
        self.gravity = 0.8
        self.ground_y = HEIGHT//2  # Ground level
        
        # Attack state
        self.is_attacking = False
        self.attack_timer = 0
        self.attack_duration = 30  # frames for attack animation
        self.current_attack_type = None  # "light" or "heavy"
        

        
    def update(self):
        # Handle input using pygame-zero keyboard
        # Movement
        previous_animation = self.current_animation
        
        # Check for light attack input
        if keyboard.j and not self.is_attacking and not self.is_jumping and not self.is_crouching:
            self.is_attacking = True
            self.attack_timer = 0
            self.current_attack_type = "light"
            self.current_animation = "light_attack"
        
        # Check for heavy attack input
        if keyboard.k and not self.is_attacking and not self.is_jumping and not self.is_crouching:
            self.is_attacking = True
            self.attack_timer = 0
            self.current_attack_type = "heavy"
            self.current_animation = "heavy_attack"
        
        # Check for jump input
        if (keyboard.up or keyboard.w or keyboard.space) and not self.is_jumping and not self.is_crouching and not self.is_attacking:
            self.is_jumping = True
            self.jump_velocity = self.jump_speed
            self.current_animation = "jump"
        
        # Check for crouch input
        if keyboard.down or keyboard.s:
            self.is_crouching = True
        else:
            self.is_crouching = False
        
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
        
        # Set animation based on state and movement
        if self.is_attacking:
            if self.current_attack_type == "heavy":
                self.current_animation = "heavy_attack"
            else:
                self.current_animation = "light_attack"
        elif self.is_jumping:
            self.current_animation = "jump"
        elif self.is_crouching:
            self.current_animation = "crouch"
        elif keyboard.left or keyboard.a:
            self.actor.x -= self.speed
            self.direction = -1
            self.actor.flip_x = True
            self.current_animation = "walk"
        elif keyboard.right or keyboard.d:
            self.actor.x += self.speed
            self.direction = 1
            self.actor.flip_x = False
            self.current_animation = "walk"
        else:
            self.current_animation = "stand"
        
        # Reset animation if switching between stand and walk
        if previous_animation != self.current_animation:
            self.reset_animation()
        
        # Keep player on screen
        self.actor.x = max(50, min(WIDTH - 50, self.actor.x))
        
        # Update animation
        frames = self.get_current_frames()
        
        # For crouch, stay on frame 2 (middle crouch pose) while key is held
        if self.current_animation == "crouch":
            self.animation_frame = 2  # Stay on crouch frame 2
        elif self.current_animation == "jump":
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
        elif self.current_animation == "stand":
            # For stand, cycle through stand frames normally
            self.animation_timer += self.animation_speed
            if self.animation_timer >= 1:
                self.animation_timer = 0
                self.animation_frame = (self.animation_frame + 1) % len(frames)
        else:
            # Normal animation cycling for walk
            self.animation_timer += self.animation_speed
            if self.animation_timer >= 1:
                self.animation_timer = 0
                self.animation_frame = (self.animation_frame + 1) % len(frames)
        
        # Set current frame with bounds checking
        if 0 <= self.animation_frame < len(frames):
            self.actor.image = frames[self.animation_frame]
            # Ensure consistent scale
            self.actor.scale = 2
    
    def get_current_frames(self):
        if self.current_animation == "walk":
            return self.walk_frames
        elif self.current_animation == "crouch":
            return self.crouch_frames
        elif self.current_animation == "jump":
            return self.jump_frames
        elif self.current_animation == "light_attack":
            return self.light_attack_frames
        elif self.current_animation == "heavy_attack":
            return self.heavy_attack_frames
        else:
            return self.stand_frames
    
    def reset_animation(self):
        """Reset animation when switching between stand and walk"""
        self.animation_frame = 0
        self.animation_timer = 0
    
    def draw(self):
        self.actor.draw()

# Create player
player = Player()

def update():
    player.update()

def draw():
    screen.fill((100, 150, 255))  # Sky blue background
    
    # Draw ground
    screen.draw.filled_rect(Rect(0, HEIGHT - 100, WIDTH, 100), (50, 200, 50))
    
    # Draw player
    player.draw()
    
    # Draw instructions
    screen.draw.text("A/D or Arrow Keys: Move", (10, 10), color="white", fontsize=20)
    screen.draw.text("S or Down Arrow: Crouch", (10, 35), color="white", fontsize=20)
    screen.draw.text("W/Up Arrow/Space: Jump", (10, 60), color="white", fontsize=20)
    screen.draw.text("J: Light Attack", (10, 85), color="white", fontsize=20)
    screen.draw.text("K: Heavy Attack", (10, 110), color="white", fontsize=20)
    screen.draw.text("JJK: Gojo's Adventure", (WIDTH//2 - 100, HEIGHT - 30), color="white", fontsize=20)

pgzrun.go() 