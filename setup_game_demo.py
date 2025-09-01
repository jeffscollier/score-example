#!/usr/bin/env python3
"""
Setup script for the Game UI Demo
================================

This script helps you install pygame and run the game demo.
"""

import subprocess
import sys
import os

def install_pygame():
    """Install pygame using pip"""
    print("Installing pygame...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
        print("✅ Pygame installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install pygame. Please install it manually:")
        print("   pip install pygame")
        return False

def check_pygame():
    """Check if pygame is already installed"""
    try:
        import pygame
        print(f"✅ Pygame is already installed (version {pygame.version.ver})")
        return True
    except ImportError:
        print("❌ Pygame is not installed")
        return False

def main():
    """Main setup function"""
    print("=" * 50)
    print("GAME UI DEMO SETUP")
    print("=" * 50)
    
    # Check if pygame is installed
    if not check_pygame():
        response = input("Would you like to install pygame now? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            if not install_pygame():
                return
        else:
            print("Please install pygame manually: pip install pygame")
            return
    
    # Check if the game file exists
    if not os.path.exists("game_ui_demo.py"):
        print("❌ game_ui_demo.py not found in current directory")
        return
    
    print("\n🎮 Ready to run the game demo!")
    print("Run: python game_ui_demo.py")
    print("\nControls:")
    print("  H - Heal (+10)")
    print("  D - Take Damage (-10)")
    print("  S - Add Score (+100)")
    print("  P - Add Power-up")
    print("  R - Reset Game")
    print("  ESC - Quit")
    
    response = input("\nWould you like to run the demo now? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        try:
            subprocess.run([sys.executable, "game_ui_demo.py"])
        except KeyboardInterrupt:
            print("\nDemo stopped by user")
        except Exception as e:
            print(f"Error running demo: {e}")

if __name__ == "__main__":
    main()
