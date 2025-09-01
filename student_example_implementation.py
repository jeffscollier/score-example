#!/usr/bin/env python3
"""
Student Example Implementation
=============================

This is a complete example of how to implement the GameLogic class.
Use this as a reference, but try to write your own version first!

This example shows:
- Variable assignments
- User input handling
- Calculations and totals
- Game state management
- Data structure usage
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
    COMPLETE EXAMPLE IMPLEMENTATION
    This shows how to implement all the required methods
    """
    
    def __init__(self):
        """
        Initialize all game variables
        This is where you set up your starting values
        """
        # Health variables
        self.health = 100
        self.max_health = 100
        self.mana = 50
        self.max_mana = 100
        
        # Status variables
        self.status = "Alive"
        self.level = 1
        self.experience = 0
        self.exp_needed = 100  # Experience needed for next level
        
        # Score and currency
        self.score = 0
        self.gold = 100
        
        # Data structures (lists)
        self.inventory = ["Health Potion", "Sword"]
        self.awards = ["First Steps"]
        
        # Calculated values (will be updated in calculate_totals)
        self.health_percentage = 100.0
        self.total_items = 2
        self.total_score = 0
    
    def get_user_input(self):
        """
        Handle user input and update game variables
        This is where you practice input() and conditional logic
        """
        print("\n" + "="*40)
        print("GAME ACTIONS")
        print("="*40)
        print("1. Heal (+20 health, -10 mana)")
        print("2. Take damage (-15 health)")
        print("3. Add item to inventory")
        print("4. Add award")
        print("5. Add score (+50)")
        print("6. Add experience (+25)")
        print("7. Use mana (-20 mana)")
        print("8. Add gold (+30)")
        print("9. Show current stats")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == "1":
            # Heal action
            if self.mana >= 10:
                self.health = min(self.max_health, self.health + 20)
                self.mana = max(0, self.mana - 10)
                print(f"Healed! Health: {self.health}, Mana: {self.mana}")
            else:
                print("Not enough mana to heal!")
                
        elif choice == "2":
            # Take damage
            self.health = max(0, self.health - 15)
            print(f"Took damage! Health: {self.health}")
            
        elif choice == "3":
            # Add item
            item = input("Enter item name: ").strip()
            if item:
                self.inventory.append(item)
                print(f"Added '{item}' to inventory!")
            else:
                print("Invalid item name!")
                
        elif choice == "4":
            # Add award
            award = input("Enter award name: ").strip()
            if award:
                self.awards.append(award)
                print(f"Earned award: '{award}'!")
            else:
                print("Invalid award name!")
                
        elif choice == "5":
            # Add score
            self.score += 50
            print(f"Score increased! New score: {self.score}")
            
        elif choice == "6":
            # Add experience
            self.experience += 25
            print(f"Experience gained! Total: {self.experience}")
            
        elif choice == "7":
            # Use mana
            if self.mana >= 20:
                self.mana -= 20
                print(f"Used mana! Remaining: {self.mana}")
            else:
                print("Not enough mana!")
                
        elif choice == "8":
            # Add gold
            self.gold += 30
            print(f"Gold added! Total: {self.gold}")
            
        elif choice == "9":
            # Show stats
            self.show_stats()
            
        else:
            print("Invalid choice! Please enter 1-9.")
    
    def show_stats(self):
        """Display current game statistics"""
        print("\n" + "="*30)
        print("CURRENT STATS")
        print("="*30)
        print(f"Health: {self.health}/{self.max_health} ({self.health_percentage:.1f}%)")
        print(f"Mana: {self.mana}/{self.max_mana}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}/{self.exp_needed}")
        print(f"Score: {self.score}")
        print(f"Gold: {self.gold}")
        print(f"Status: {self.status}")
        print(f"Inventory items: {len(self.inventory)}")
        print(f"Awards: {len(self.awards)}")
        
        if self.inventory:
            print("\nInventory:")
            for item in self.inventory:
                print(f"  • {item}")
        
        if self.awards:
            print("\nAwards:")
            for award in self.awards:
                print(f"  🏆 {award}")
    
    def calculate_totals(self):
        """
        Calculate derived values and totals
        This is where you practice mathematical operations
        """
        # Calculate health percentage
        self.health_percentage = (self.health / self.max_health) * 100
        
        # Calculate total inventory items
        self.total_items = len(self.inventory)
        
        # Calculate total score including level bonus
        self.total_score = self.score + (self.level * 10)
        
        # Calculate mana percentage
        self.mana_percentage = (self.mana / self.max_mana) * 100
        
        # Calculate experience progress
        self.exp_progress = (self.experience / self.exp_needed) * 100
    
    def update_game_state(self):
        """
        Update game state based on current variables
        This is where you practice conditional logic
        """
        # Check if player is dead
        if self.health <= 0:
            self.status = "Dead"
            print("💀 You died! Game over!")
        
        # Check if player leveled up
        if self.experience >= self.exp_needed:
            self.level += 1
            self.experience = 0
            self.exp_needed = self.level * 100  # Increase requirement
            self.status = "Leveled Up!"
            print(f"🎉 Level up! New level: {self.level}")
            
            # Restore some health and mana on level up
            self.health = min(self.max_health, self.health + 30)
            self.mana = min(self.max_mana, self.mana + 20)
        
        # Check for score-based awards
        if self.score >= 500 and "High Scorer" not in self.awards:
            self.awards.append("High Scorer")
            print("🏆 New award: High Scorer!")
        
        if self.score >= 1000 and "Score Master" not in self.awards:
            self.awards.append("Score Master")
            print("🏆 New award: Score Master!")
        
        # Check for inventory-based awards
        if len(self.inventory) >= 5 and "Collector" not in self.awards:
            self.awards.append("Collector")
            print("🏆 New award: Collector!")
        
        if len(self.inventory) >= 10 and "Hoarder" not in self.awards:
            self.awards.append("Hoarder")
            print("🏆 New award: Hoarder!")
        
        # Check for level-based awards
        if self.level >= 5 and "Experienced" not in self.awards:
            self.awards.append("Experienced")
            print("🏆 New award: Experienced!")
        
        if self.level >= 10 and "Veteran" not in self.awards:
            self.awards.append("Veteran")
            print("🏆 New award: Veteran!")
        
        # Check for gold-based awards
        if self.gold >= 500 and "Rich" not in self.awards:
            self.awards.append("Rich")
            print("🏆 New award: Rich!")
        
        # Update status if not dead or leveled up
        if self.status not in ["Dead", "Leveled Up!"]:
            if self.health_percentage > 80:
                self.status = "Excellent"
            elif self.health_percentage > 50:
                self.status = "Good"
            elif self.health_percentage > 25:
                self.status = "Injured"
            else:
                self.status = "Critical"
    
    def get_display_data(self):
        """
        Return all data needed for the graphical display
        This is where you practice returning dictionaries
        """
        return {
            'health': {
                'current': self.health,
                'max': self.max_health,
                'percentage': self.health_percentage
            },
            'mana': {
                'current': self.mana,
                'max': self.max_mana,
                'percentage': self.mana_percentage
            },
            'status': self.status,
            'score': self.total_score,
            'inventory': self.inventory,
            'awards': self.awards,
            'level': self.level,
            'experience': self.experience,
            'gold': self.gold,
            'exp_progress': self.exp_progress
        }

class GameDisplay:
    """
    GRAPHICS SECTION: This is handled automatically
    """
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Student Game Development - Example Implementation")
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
        if percentage > 80:
            color = GREEN
        elif percentage > 50:
            color = YELLOW
        elif percentage > 25:
            color = ORANGE
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
    
    def draw_mana_bar(self, x, y, width, height, mana_data):
        """Draw mana bar"""
        current = mana_data['current']
        max_mana = mana_data['max']
        percentage = mana_data['percentage']
        
        # Background
        pygame.draw.rect(self.screen, (50, 50, 100), (x, y, width, height))
        
        # Mana bar
        bar_width = int(width * (percentage / 100))
        color = BLUE
        pygame.draw.rect(self.screen, color, (x, y, bar_width, height))
        pygame.draw.rect(self.screen, WHITE, (x, y, width, height), 2)
        
        # Mana text
        mana_text = f"{current}/{max_mana} ({percentage:.1f}%)"
        text_surface = self.small_font.render(mana_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(x + width//2, y + height//2))
        self.screen.blit(text_surface, text_rect)
    
    def draw_status_panel(self, x, y, status_data):
        """Draw player status information"""
        # Status background
        status_bg = pygame.Rect(x, y, 300, 180)
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
        
        # Gold
        gold_text = self.small_font.render(f"Gold: {status_data['gold']}", True, GOLD)
        self.screen.blit(gold_text, (x + 10, y + 80))
        
        # Experience progress bar
        exp_bg = pygame.Rect(x + 10, y + 100, 280, 20)
        pygame.draw.rect(self.screen, (50, 50, 50), exp_bg)
        exp_width = int(280 * (status_data['exp_progress'] / 100))
        pygame.draw.rect(self.screen, YELLOW, (x + 10, y + 100, exp_width, 20))
        pygame.draw.rect(self.screen, WHITE, exp_bg, 1)
    
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
            "EXAMPLE IMPLEMENTATION",
            "Press SPACE to run game logic",
            "Press R to reset game state",
            "Press ESC to quit",
            "",
            "This shows a complete implementation",
            "of the GameLogic class methods"
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
        title = self.large_font.render("Example Implementation - Your Game Logic!", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 30))
        self.screen.blit(title, title_rect)
        
        # Draw health bar
        self.draw_health_bar(50, 80, 300, 40, game_data['health'])
        
        # Draw mana bar
        self.draw_mana_bar(50, 130, 300, 30, game_data['mana'])
        
        # Draw status panel
        self.draw_status_panel(50, 180, game_data)
        
        # Draw score panel
        self.draw_score_panel(400, 180, game_data['score'])
        
        # Draw inventory panel
        self.draw_inventory_panel(50, 380, game_data['inventory'])
        
        # Draw awards panel
        self.draw_awards_panel(400, 380, game_data['awards'])
        
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
                print("RUNNING EXAMPLE GAME LOGIC...")
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
        print("STUDENT GAME DEVELOPMENT - EXAMPLE IMPLEMENTATION")
        print("="*60)
        print("This shows a complete implementation of the GameLogic class!")
        print()
        print("CONTROLS:")
        print("  SPACE - Run the example game logic")
        print("  R - Reset game state")
        print("  ESC - Quit")
        print()
        print("This example demonstrates:")
        print("• Variable assignments and calculations")
        print("• User input handling")
        print("• Data structure management")
        print("• Conditional logic")
        print("• Function return values")
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
