#!/usr/bin/env python3
"""
Student Game Development Template
================================

This template is designed for learning Python game development.
You (the student) will write the game logic in the GameLogic class,
while the graphical display is handled automatically.

Your job: Write the game logic and variable management
My job: Handle the graphics and display

Learning Focus: Variables, calculations, user input, data structures
"""

import pygame
import sys
import math
from typing import Dict, List, Any

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors
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
LIGHT_BLUE = (173, 216, 230)
GOLD = (255, 215, 0)

class GameLogic:
    """
    STUDENT SECTION: Write your game logic here!
    
    This is where you'll practice:
    - Variable assignments
    - Calculations and totals
    - User input handling
    - Data structure management
    """
    
    def __init__(self):
        """
        TODO: Initialize your game variables here
        Hint: Think about what a player needs in a game
        """
        # TODO: Create variables for player health
        # Example: self.health = 100
        
        # TODO: Create variables for player status
        # Example: self.status = "Alive"
        
        # TODO: Create variables for player score
        # Example: self.score = 0
        
        # TODO: Create a list for player inventory
        # Example: self.inventory = []
        
        # TODO: Create a list for player awards
        # Example: self.awards = []
        
        # TODO: Add any other variables you think a player needs
        # Example: self.level = 1, self.experience = 0, etc.
        
        pass  # Remove this when you add your variables
    
    def get_user_input(self):
        """
        TODO: Handle user input for game actions
        This function should ask the user what they want to do and update game variables
        
        Hint: Use input() to get user choices
        Example actions: heal, take damage, add item, add award, etc.
        """
        # TODO: Print available actions to the user
        # TODO: Get user input with input()
        # TODO: Use if/elif statements to handle different actions
        # TODO: Update your game variables based on user choices
        
        pass  # Remove this when you implement user input
    
    def calculate_totals(self):
        """
        TODO: Calculate any totals or derived values
        This function should compute values based on your other variables
        
        Examples:
        - Total inventory value
        - Health percentage
        - Experience needed for next level
        - Total score including bonuses
        """
        # TODO: Calculate health percentage
        # TODO: Calculate total inventory items
        # TODO: Calculate any other totals you need
        
        pass  # Remove this when you implement calculations
    
    def update_game_state(self):
        """
        TODO: Update game state based on current variables
        This function should check conditions and update status
        
        Examples:
        - Check if player is dead (health <= 0)
        - Check if player leveled up
        - Check if player earned new awards
        """
        # TODO: Check if player is dead
        # TODO: Check if player leveled up
        # TODO: Check for new awards
        # TODO: Update status based on conditions
        
        pass  # Remove this when you implement game state updates
    
    def get_display_data(self):
        """
        TODO: Return all data needed for the graphical display
        This function should return a dictionary with all the information
        the graphics system needs to display
        
        The graphics system expects this format:
        {
            'health': {'current': 100, 'max': 100, 'percentage': 100},
            'status': 'Alive',
            'score': 0,
            'inventory': ['item1', 'item2'],
            'awards': ['award1', 'award2'],
            'level': 1,
            'experience': 0
        }
        """
        # TODO: Calculate health percentage
        # TODO: Return a dictionary with all your game data
        
        # Example return (replace with your actual data):
        return {
            'health': {'current': 100, 'max': 100, 'percentage': 100},
            'status': 'Alive',
            'score': 0,
            'inventory': [],
            'awards': [],
            'level': 1,
            'experience': 0
        }

class GameDisplay:
    """
    GRAPHICS SECTION: This is handled automatically
    You don't need to modify this section - it reads from your GameLogic class
    """
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Student Game Development - Your Game Logic in Action!")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.large_font = pygame.font.Font(None, 48)
        
        # Animation variables
        self.animation_frame = 0
        
    def draw_health_bar(self, x, y, width, height, health_data):
        """Draw health bar with color changes"""
        current = health_data['current']
        max_health = health_data['max']
        percentage = health_data['percentage']
        
        # Background
        pygame.draw.rect(self.screen, DARK_RED, (x, y, width, height))
        
        # Health bar
        bar_width = int(width * (percentage / 100))
        if percentage > 60:
            color = GREEN
        elif percentage > 30:
            color = YELLOW
        else:
            color = RED
            # Pulsing effect when low
            pulse = int(50 * math.sin(self.animation_frame * 0.1))
            color = (min(255, color[0] + pulse), color[1], color[2])
        
        pygame.draw.rect(self.screen, color, (x, y, bar_width, height))
        pygame.draw.rect(self.screen, WHITE, (x, y, width, height), 2)
        
        # Health text
        health_text = f"{current}/{max_health} ({percentage:.1f}%)"
        text_surface = self.small_font.render(health_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x + width//2, y + height//2))
        self.screen.blit(text_surface, text_rect)
    
    def draw_status_panel(self, x, y, status_data):
        """Draw player status information"""
        # Status background
        status_bg = pygame.Rect(x, y, 300, 150)
        pygame.draw.rect(self.screen, GRAY, status_bg)
        pygame.draw.rect(self.screen, WHITE, status_bg, 2)
        
        # Status text
        status_text = self.font.render(f"Status: {status_data['status']}", True, WHITE)
        self.screen.blit(status_text, (x + 10, y + 10))
        
        # Level
        level_text = self.small_font.render(f"Level: {status_data['level']}", True, WHITE)
        self.screen.blit(level_text, (x + 10, y + 40))
        
        # Experience
        exp_text = self.small_font.render(f"Experience: {status_data['experience']}", True, WHITE)
        self.screen.blit(exp_text, (x + 10, y + 60))
    
    def draw_score_panel(self, x, y, score_data):
        """Draw score display"""
        # Score background
        score_bg = pygame.Rect(x, y, 200, 80)
        pygame.draw.rect(self.screen, BLUE, score_bg)
        pygame.draw.rect(self.screen, WHITE, score_bg, 2)
        
        # Score text
        score_text = self.font.render(f"Score: {score_data}", True, WHITE)
        text_rect = score_text.get_rect(center=(x + 100, y + 40))
        self.screen.blit(score_text, text_rect)
    
    def draw_inventory_panel(self, x, y, inventory_data):
        """Draw inventory display"""
        # Inventory background
        inv_bg = pygame.Rect(x, y, 300, 200)
        pygame.draw.rect(self.screen, DARK_GREEN, inv_bg)
        pygame.draw.rect(self.screen, WHITE, inv_bg, 2)
        
        # Inventory title
        inv_title = self.font.render("Inventory", True, WHITE)
        self.screen.blit(inv_title, (x + 10, y + 10))
        
        # Inventory items
        if inventory_data:
            for i, item in enumerate(inventory_data):
                if i < 8:  # Limit display to 8 items
                    item_text = self.small_font.render(f"• {item}", True, YELLOW)
                    self.screen.blit(item_text, (x + 20, y + 40 + i * 20))
        else:
            no_items = self.small_font.render("No items", True, GRAY)
            self.screen.blit(no_items, (x + 20, y + 40))
    
    def draw_awards_panel(self, x, y, awards_data):
        """Draw awards display"""
        # Awards background
        awards_bg = pygame.Rect(x, y, 300, 200)
        pygame.draw.rect(self.screen, PURPLE, awards_bg)
        pygame.draw.rect(self.screen, WHITE, awards_bg, 2)
        
        # Awards title
        awards_title = self.font.render("Awards", True, WHITE)
        self.screen.blit(awards_title, (x + 10, y + 10))
        
        # Awards list
        if awards_data:
            for i, award in enumerate(awards_data):
                if i < 8:  # Limit display to 8 awards
                    award_text = self.small_font.render(f"🏆 {award}", True, GOLD)
                    self.screen.blit(award_text, (x + 20, y + 40 + i * 20))
        else:
            no_awards = self.small_font.render("No awards yet", True, GRAY)
            self.screen.blit(no_awards, (x + 20, y + 40))
    
    def draw_instructions(self):
        """Draw learning instructions"""
        instructions = [
            "STUDENT LEARNING MODE",
            "Press SPACE to run your game logic",
            "Press R to reset game state",
            "Press ESC to quit",
            "",
            "Your job: Write the game logic in GameLogic class",
            "My job: Display your variables graphically"
        ]
        
        y_offset = SCREEN_HEIGHT - 200
        for i, instruction in enumerate(instructions):
            color = YELLOW if i == 0 else WHITE
            font = self.large_font if i == 0 else self.small_font
            text = font.render(instruction, True, color)
            self.screen.blit(text, (10, y_offset + i * 25))
    
    def draw(self, game_data):
        """Draw everything to the screen"""
        self.screen.fill(BLACK)
        
        # Draw title
        title = self.large_font.render("Your Game Logic in Action!", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 30))
        self.screen.blit(title, title_rect)
        
        # Draw health bar
        self.draw_health_bar(50, 80, 300, 40, game_data['health'])
        
        # Draw status panel
        self.draw_status_panel(50, 150, game_data)
        
        # Draw score panel
        self.draw_score_panel(400, 150, game_data['score'])
        
        # Draw inventory panel
        self.draw_inventory_panel(50, 320, game_data['inventory'])
        
        # Draw awards panel
        self.draw_awards_panel(400, 320, game_data['awards'])
        
        # Draw instructions
        self.draw_instructions()
        
        # Draw decorative elements
        pygame.draw.circle(self.screen, GREEN, (800, 100), 20)
        pygame.draw.circle(self.screen, RED, (850, 100), 20)
        pygame.draw.circle(self.screen, BLUE, (825, 130), 15)
        
        pygame.display.flip()
    
    def update(self):
        """Update animation frame"""
        self.animation_frame += 1

class GameApp:
    """
    MAIN APPLICATION: This coordinates between your game logic and the display
    """
    
    def __init__(self):
        self.game_logic = GameLogic()
        self.display = GameDisplay()
        self.running = True
        
    def handle_input(self, event):
        """Handle keyboard input"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Run student's game logic
                print("\n" + "="*50)
                print("RUNNING YOUR GAME LOGIC...")
                print("="*50)
                self.game_logic.get_user_input()
                self.game_logic.calculate_totals()
                self.game_logic.update_game_state()
                print("Game logic completed!")
                
            elif event.key == pygame.K_r:  # Reset
                print("Resetting game state...")
                self.game_logic = GameLogic()
                
            elif event.key == pygame.K_ESCAPE:  # Quit
                return False
        return True
    
    def run(self):
        """Main game loop"""
        print("="*60)
        print("STUDENT GAME DEVELOPMENT TEMPLATE")
        print("="*60)
        print("This template helps you learn Python game development!")
        print()
        print("YOUR TASK:")
        print("1. Write game logic in the GameLogic class")
        print("2. Press SPACE to run your code")
        print("3. See your variables displayed graphically")
        print()
        print("CONTROLS:")
        print("  SPACE - Run your game logic")
        print("  R - Reset game state")
        print("  ESC - Quit")
        print()
        print("Start by implementing the GameLogic class methods!")
        print("="*60)
        
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.running = self.handle_input(event)
            
            # Update display
            self.display.update()
            
            # Get game data and draw
            game_data = self.game_logic.get_display_data()
            self.display.draw(game_data)
            
            # Control frame rate
            self.display.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

def main():
    """Main function"""
    try:
        app = GameApp()
        app.run()
    except pygame.error as e:
        print(f"Error: {e}")
        print("Make sure pygame is installed: pip install pygame")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
