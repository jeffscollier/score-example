#!/usr/bin/env python3
"""
Simple Game UI Demo with Pygame
===============================

A quick and easy graphical display showing:
- Player health bar
- Player status
- Score system
- Interactive controls

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

class GameUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game UI Demo - Health, Status & Score")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Game state
        self.player_health = 100
        self.max_health = 100
        self.score = 0
        self.status = "Alive"
        self.power_ups = []
        self.level = 1
        
        # Animation variables
        self.health_pulse = 0
        self.score_animation = 0
        
    def draw_health_bar(self, x, y, width, height, current_health, max_health):
        """Draw a health bar with color changes based on health level"""
        # Background (dark red)
        pygame.draw.rect(self.screen, DARK_RED, (x, y, width, height))
        
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
            pulse = int(50 * math.sin(self.health_pulse * 0.1))
            color = (min(255, color[0] + pulse), color[1], color[2])
        
        # Draw health bar
        pygame.draw.rect(self.screen, color, (x, y, bar_width, height))
        
        # Draw border
        pygame.draw.rect(self.screen, WHITE, (x, y, width, height), 2)
        
        # Draw health text
        health_text = f"{current_health}/{max_health}"
        text_surface = self.small_font.render(health_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x + width//2, y + height//2))
        self.screen.blit(text_surface, text_rect)
    
    def draw_status_panel(self, x, y):
        """Draw player status information"""
        # Status background
        status_bg = pygame.Rect(x, y, 300, 120)
        pygame.draw.rect(self.screen, GRAY, status_bg)
        pygame.draw.rect(self.screen, WHITE, status_bg, 2)
        
        # Status text
        status_text = self.font.render(f"Status: {self.status}", True, WHITE)
        self.screen.blit(status_text, (x + 10, y + 10))
        
        # Level
        level_text = self.small_font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (x + 10, y + 40))
        
        # Power-ups
        if self.power_ups:
            power_text = self.small_font.render("Power-ups:", True, WHITE)
            self.screen.blit(power_text, (x + 10, y + 60))
            
            for i, power_up in enumerate(self.power_ups):
                power_item = self.small_font.render(f"• {power_up}", True, YELLOW)
                self.screen.blit(power_item, (x + 20, y + 80 + i * 20))
        else:
            no_power_text = self.small_font.render("No power-ups active", True, GRAY)
            self.screen.blit(no_power_text, (x + 10, y + 60))
    
    def draw_score_panel(self, x, y):
        """Draw score display with animation"""
        # Score background
        score_bg = pygame.Rect(x, y, 200, 80)
        pygame.draw.rect(self.screen, BLUE, score_bg)
        pygame.draw.rect(self.screen, WHITE, score_bg, 2)
        
        # Score text with animation
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        
        # Add a subtle animation when score changes
        if self.score_animation > 0:
            scale = 1.0 + (self.score_animation * 0.1)
            # Simple scaling effect
            score_text = pygame.transform.scale(score_text, 
                (int(score_text.get_width() * scale), 
                 int(score_text.get_height() * scale)))
            self.score_animation -= 1
        
        text_rect = score_text.get_rect(center=(x + 100, y + 40))
        self.screen.blit(score_text, text_rect)
    
    def draw_controls_info(self):
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
            font = self.font if i == 0 else self.small_font
            text = font.render(control, True, color)
            self.screen.blit(text, (10, y_offset + i * 25))
    
    def add_power_up(self):
        """Add a random power-up"""
        power_ups_list = ["Speed Boost", "Shield", "Double Points", "Health Regen", "Fire Power"]
        import random
        new_power = random.choice(power_ups_list)
        if new_power not in self.power_ups:
            self.power_ups.append(new_power)
            # Limit to 3 power-ups
            if len(self.power_ups) > 3:
                self.power_ups.pop(0)
    
    def update(self):
        """Update game state and animations"""
        self.health_pulse += 1
        
        # Auto-remove power-ups after some time (simplified)
        if len(self.power_ups) > 0 and self.health_pulse % 300 == 0:
            self.power_ups.pop(0)
    
    def handle_input(self, event):
        """Handle keyboard input"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # Heal
                self.player_health = min(self.max_health, self.player_health + 10)
            elif event.key == pygame.K_d:  # Take damage
                self.player_health = max(0, self.player_health - 10)
                if self.player_health <= 0:
                    self.status = "Dead"
            elif event.key == pygame.K_s:  # Add score
                self.score += 100
                self.score_animation = 10
            elif event.key == pygame.K_p:  # Add power-up
                self.add_power_up()
            elif event.key == pygame.K_r:  # Reset
                self.reset_game()
            elif event.key == pygame.K_ESCAPE:  # Quit
                return False
        return True
    
    def reset_game(self):
        """Reset game to initial state"""
        self.player_health = 100
        self.score = 0
        self.status = "Alive"
        self.power_ups = []
        self.level = 1
        self.health_pulse = 0
        self.score_animation = 0
    
    def draw(self):
        """Draw everything to the screen"""
        self.screen.fill(BLACK)
        
        # Draw title
        title = self.font.render("Game UI Demo", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 30))
        self.screen.blit(title, title_rect)
        
        # Draw health bar
        self.draw_health_bar(50, 80, 300, 40, self.player_health, self.max_health)
        
        # Draw status panel
        self.draw_status_panel(50, 150)
        
        # Draw score panel
        self.draw_score_panel(400, 150)
        
        # Draw controls info
        self.draw_controls_info()
        
        # Draw some decorative elements
        pygame.draw.circle(self.screen, GREEN, (700, 100), 20)
        pygame.draw.circle(self.screen, RED, (750, 100), 20)
        pygame.draw.circle(self.screen, BLUE, (725, 130), 15)
        
        pygame.display.flip()
    
    def run(self):
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
                    running = self.handle_input(event)
            
            # Update game state
            self.update()
            
            # Draw everything
            self.draw()
            
            # Control frame rate
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

def main():
    """Main function"""
    print("=" * 50)
    print("PYGAME GAME UI DEMO")
    print("=" * 50)
    print("This demo shows a simple game UI with:")
    print("• Health bar with color changes")
    print("• Player status display")
    print("• Score system with animation")
    print("• Interactive controls")
    print()
    print("Make sure you have pygame installed:")
    print("pip install pygame")
    print()
    
    try:
        game = GameUI()
        game.run()
    except pygame.error as e:
        print(f"Error: {e}")
        print("Make sure pygame is installed: pip install pygame")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
