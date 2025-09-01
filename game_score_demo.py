#!/usr/bin/env python3
"""
Simple Game UI Demo with Pygame - Procedural Version
===================================================

A quick and easy graphical display showing:
- Player health bar
- Player status
- Score system
- Interactive controls

This version uses procedural programming instead of classes.
Requirements: pip install pygame
"""

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)
DARK_GREEN = (0, 128, 0)
DARK_RED = (128, 0, 0)

# ========================================
# STUDENT TEMPLATE: GAME VARIABLES SECTION
# ========================================
# This is where you define all your game variables
# These are the core data that your game tracks and displays

# Global game state variables
player_health = 100      # Current player health
max_health = 100         # Maximum possible health
score = 0                # Player's current score
status = "Alive"         # Player's current status
power_ups = []           # List of active power-ups
level = 1                # Player's current level

# Animation variables
health_pulse = 0         # Counter for health bar animation
score_animation = 0      # Counter for score animation effect

# Pygame objects
screen = None
clock = None
font = None
small_font = None

def initialize_pygame():
    """Initialize pygame display and fonts"""
    global screen, clock, font, small_font
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game UI Demo - Health, Status & Score")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

def draw_health_bar(x, y, width, height, current_health, max_health):
    """Draw a health bar with color changes based on health level"""
    global health_pulse
    
    # Background (dark red)
    pygame.draw.rect(screen, DARK_RED, (x, y, width, height))
    
    # Calculate health percentage and bar width
    health_percentage = current_health / max_health
    bar_width = int(width * health_percentage)
    
    # Choose color based on health level
    if health_percentage > 0.6:
        color = GREEN
    elif health_percentage > 0.3:
        color = YELLOW
    else:
        color = RED
        # Add pulsing effect when health is low
        pulse = int(50 * math.sin(health_pulse * 0.1))
        color = (min(255, color[0] + pulse), color[1], color[2])
    
    # Draw health bar
    pygame.draw.rect(screen, color, (x, y, bar_width, height))
    
    # Draw border
    pygame.draw.rect(screen, WHITE, (x, y, width, height), 2)
    
    # Draw health text
    health_text = f"{current_health}/{max_health}"
    text_surface = small_font.render(health_text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width//2, y + height//2))
    screen.blit(text_surface, text_rect)

def draw_status_panel(x, y):
    """Draw player status information"""
    global status, level, power_ups
    
    # Status background
    status_bg = pygame.Rect(x, y, 300, 120)
    pygame.draw.rect(screen, GRAY, status_bg)
    pygame.draw.rect(screen, WHITE, status_bg, 2)
    
    # Status text
    status_text = font.render(f"Status: {status}", True, WHITE)
    screen.blit(status_text, (x + 10, y + 10))
    
    # Level
    level_text = small_font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (x + 10, y + 40))
    
    # Power-ups
    if power_ups:
        power_text = small_font.render("Power-ups:", True, WHITE)
        screen.blit(power_text, (x + 10, y + 60))
        
        for i, power_up in enumerate(power_ups):
            power_item = small_font.render(f"• {power_up}", True, YELLOW)
            screen.blit(power_item, (x + 20, y + 80 + i * 20))
    else:
        no_power_text = small_font.render("No power-ups active", True, GRAY)
        screen.blit(no_power_text, (x + 10, y + 60))

# ========================================
# STUDENT TEMPLATE: SCORE DISPLAY SECTION
# ========================================
# This is where the score is displayed on screen
# The score variable is read and shown to the player

def draw_score_panel(x, y):
    """Draw score display with animation"""
    global score_animation, score
    
    # Score background
    score_bg = pygame.Rect(x, y, 200, 80)
    pygame.draw.rect(screen, BLUE, score_bg)
    pygame.draw.rect(screen, WHITE, score_bg, 2)
    
    # Score text with animation
    score_text = font.render(f"Score: {score}", True, WHITE)  # STUDENT: This displays the score variable
    
    # Add a subtle animation when score changes
    if score_animation > 0:                                    # STUDENT: Animation effect when score changes
        scale = 1.0 + (score_animation * 0.1)
        # Simple scaling effect
        score_text = pygame.transform.scale(score_text, 
            (int(score_text.get_width() * scale), 
             int(score_text.get_height() * scale)))
        score_animation -= 1                                   # STUDENT: Count down animation
    
    text_rect = score_text.get_rect(center=(x + 100, y + 40))
    screen.blit(score_text, text_rect)

def draw_controls_info():
    """Draw control instructions"""
    controls = [
        "Controls:",
        "H - Heal (+10)",
        "D - Take Damage (-10)",
        "S - Add Score (+100)",
        "P - Add Power-up",
        "R - Reset Game",
        "ESC - Quit"
    ]
    
    y_offset = SCREEN_HEIGHT - 200
    for i, control in enumerate(controls):
        color = YELLOW if i == 0 else WHITE
        font_to_use = font if i == 0 else small_font
        text = font_to_use.render(control, True, color)
        screen.blit(text, (10, y_offset + i * 25))

def add_power_up():
    """Add a random power-up"""
    global power_ups
    power_ups_list = ["Speed Boost", "Shield", "Double Points", "Health Regen", "Fire Power"]
    import random
    new_power = random.choice(power_ups_list)
    if new_power not in power_ups:
        power_ups.append(new_power)
        # Limit to 3 power-ups
        if len(power_ups) > 3:
            power_ups.pop(0)

# ========================================
# STUDENT TEMPLATE: GAME STATE UPDATE SECTION
# ========================================
# This is where you update game variables over time
# This runs every frame and can change variables automatically

def update_game_state():
    """Update game state and animations"""
    global health_pulse, power_ups
    
    health_pulse += 1                    # STUDENT: Animation counter increases every frame
    
    # Auto-remove power-ups after some time (simplified)
    if len(power_ups) > 0 and health_pulse % 300 == 0:  # STUDENT: Every 300 frames (5 seconds)
        power_ups.pop(0)                                 # STUDENT: Remove oldest power-up

# ========================================
# STUDENT TEMPLATE: USER INPUT SECTION
# ========================================
# This is where you handle user input and update game variables
# When a key is pressed, you modify the game state variables

def handle_input(event):
    """Handle keyboard input"""
    global player_health, score, status, score_animation
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_h:  # Heal
            player_health = min(max_health, player_health + 10)
        elif event.key == pygame.K_d:  # Take damage
            player_health = max(0, player_health - 10)
            if player_health <= 0:
                status = "Dead"
        elif event.key == pygame.K_s:  # Add score
            score += 100                    # STUDENT: This is where score increases
            score_animation = 10            # STUDENT: This triggers the animation
        elif event.key == pygame.K_p:  # Add power-up
            add_power_up()
        elif event.key == pygame.K_r:  # Reset
            reset_game()
        elif event.key == pygame.K_ESCAPE:  # Quit
            return False
    return True

# ========================================
# STUDENT TEMPLATE: GAME STATE RESET SECTION
# ========================================
# This is where you reset all game variables to their starting values
# This is like starting a new game

def reset_game():
    """Reset game to initial state"""
    global player_health, score, status, power_ups, level, health_pulse, score_animation
    
    player_health = 100      # STUDENT: Reset health to full
    score = 0                # STUDENT: Reset score to zero
    status = "Alive"         # STUDENT: Reset status to alive
    power_ups = []           # STUDENT: Clear all power-ups
    level = 1                # STUDENT: Reset level to 1
    health_pulse = 0         # STUDENT: Reset animation counters
    score_animation = 0

def draw_everything():
    """Draw everything to the screen"""
    global player_health, max_health
    
    screen.fill(BLACK)
    
    # Draw title
    title = font.render("Game UI Demo", True, WHITE)
    title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 30))
    screen.blit(title, title_rect)
    
    # Draw health bar
    draw_health_bar(50, 80, 300, 40, player_health, max_health)
    
    # Draw status panel
    draw_status_panel(50, 150)
    
    # Draw score panel
    draw_score_panel(400, 150)
    
    # Draw controls info
    draw_controls_info()
    
    # Draw some decorative elements
    pygame.draw.circle(screen, GREEN, (700, 100), 20)
    pygame.draw.circle(screen, RED, (750, 100), 20)
    pygame.draw.circle(screen, BLUE, (725, 130), 15)
    
    pygame.display.flip()

def run_game():
    """Main game loop"""
    running = True
    
    print("Game UI Demo Started!")
    print("Use the keyboard controls to interact with the game elements.")
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                running = handle_input(event)
        
        # Update game state
        update_game_state()
        
        # Draw everything
        draw_everything()
        
        # Control frame rate
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

def main():
    """Main function"""
    print("=" * 50)
    print("PYGAME GAME UI DEMO - PROCEDURAL VERSION")
    print("=" * 50)
    print("This demo shows a simple game UI with:")
    print("• Health bar with color changes")
    print("• Player status display")
    print("• Score system with animation")
    print("• Interactive controls")
    print("• Procedural programming (no classes)")
    print()
    print("Make sure you have pygame installed:")
    print("pip install pygame")
    print()
    
    try:
        initialize_pygame()
        run_game()
    except pygame.error as e:
        print(f"Error: {e}")
        print("Make sure pygame is installed: pip install pygame")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
