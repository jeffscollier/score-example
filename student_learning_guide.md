# Student Game Development Learning Guide

## 🎯 Your Learning Objectives

By completing this project, you'll learn:
- **Variable assignments** and data types
- **User input** handling with `input()`
- **Calculations** and mathematical operations
- **Data structures** (lists, dictionaries)
- **Conditional logic** (if/elif/else)
- **Function definitions** and return values
- **Object-oriented programming** basics

## 📝 Step-by-Step Implementation Guide

### Step 1: Initialize Your Game Variables

In the `__init__` method, create variables to track:

```python
def __init__(self):
    # Health variables
    self.health = 100
    self.max_health = 100
    
    # Status variables
    self.status = "Alive"
    self.level = 1
    self.experience = 0
    
    # Score variables
    self.score = 0
    
    # Data structures (lists)
    self.inventory = []
    self.awards = []
    
    # Additional variables you might want
    self.gold = 0
    self.mana = 50
    self.max_mana = 100
```

### Step 2: Handle User Input

In the `get_user_input` method, create a menu system:

```python
def get_user_input(self):
    print("\nWhat would you like to do?")
    print("1. Heal (+20 health)")
    print("2. Take damage (-15 health)")
    print("3. Add item to inventory")
    print("4. Add award")
    print("5. Add score (+50)")
    print("6. Add experience (+25)")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        self.health = min(self.max_health, self.health + 20)
        print(f"Healed! Health: {self.health}")
        
    elif choice == "2":
        self.health = max(0, self.health - 15)
        print(f"Took damage! Health: {self.health}")
        
    elif choice == "3":
        item = input("Enter item name: ")
        self.inventory.append(item)
        print(f"Added {item} to inventory!")
        
    elif choice == "4":
        award = input("Enter award name: ")
        self.awards.append(award)
        print(f"Earned award: {award}!")
        
    elif choice == "5":
        self.score += 50
        print(f"Score increased! New score: {self.score}")
        
    elif choice == "6":
        self.experience += 25
        print(f"Experience gained! Total: {self.experience}")
        
    else:
        print("Invalid choice!")
```

### Step 3: Calculate Totals and Derived Values

In the `calculate_totals` method:

```python
def calculate_totals(self):
    # Calculate health percentage
    self.health_percentage = (self.health / self.max_health) * 100
    
    # Calculate total inventory items
    self.total_items = len(self.inventory)
    
    # Calculate experience needed for next level
    self.exp_needed = self.level * 100
    
    # Calculate total score including bonuses
    self.total_score = self.score + (self.level * 10)
```

### Step 4: Update Game State

In the `update_game_state` method:

```python
def update_game_state(self):
    # Check if player is dead
    if self.health <= 0:
        self.status = "Dead"
        print("You died!")
    
    # Check if player leveled up
    if self.experience >= self.exp_needed:
        self.level += 1
        self.experience = 0
        self.status = "Leveled Up!"
        print(f"Level up! New level: {self.level}")
    
    # Check for new awards based on score
    if self.score >= 500 and "High Scorer" not in self.awards:
        self.awards.append("High Scorer")
        print("New award: High Scorer!")
    
    # Check for inventory-based awards
    if len(self.inventory) >= 5 and "Collector" not in self.awards:
        self.awards.append("Collector")
        print("New award: Collector!")
```

### Step 5: Return Display Data

In the `get_display_data` method:

```python
def get_display_data(self):
    return {
        'health': {
            'current': self.health,
            'max': self.max_health,
            'percentage': self.health_percentage
        },
        'status': self.status,
        'score': self.total_score,
        'inventory': self.inventory,
        'awards': self.awards,
        'level': self.level,
        'experience': self.experience
    }
```

## 🎮 How to Use the Template

1. **Install pygame**: `pip install pygame`
2. **Run the template**: `python student_game_template.py`
3. **Implement the GameLogic class** methods
4. **Press SPACE** to run your game logic
5. **See your variables** displayed graphically
6. **Press R** to reset and try again

## 💡 Learning Tips

### Variable Assignment Practice
```python
# Basic assignments
self.health = 100
self.score = 0

# Calculations
self.health = self.health + 20
self.score = self.score * 2

# Using functions
self.health = max(0, self.health - 10)  # Prevent negative health
self.health = min(self.max_health, self.health + 20)  # Prevent over-healing
```

### List Operations Practice
```python
# Adding items
self.inventory.append("Sword")
self.inventory.append("Potion")

# Checking if item exists
if "Sword" in self.inventory:
    print("You have a sword!")

# Counting items
item_count = len(self.inventory)

# Removing items
if "Potion" in self.inventory:
    self.inventory.remove("Potion")
```

### Conditional Logic Practice
```python
# Simple conditions
if self.health > 50:
    self.status = "Healthy"
elif self.health > 25:
    self.status = "Injured"
else:
    self.status = "Critical"

# Multiple conditions
if self.score >= 1000 and self.level >= 5:
    self.awards.append("Master Player")
```

## 🚀 Advanced Challenges

Once you've mastered the basics, try these challenges:

1. **Add a shop system** where players can buy items with gold
2. **Create a combat system** with damage calculations
3. **Add item effects** that modify health, mana, or score
4. **Implement a save/load system** using files
5. **Create different character classes** with different stats

## 📚 Key Python Concepts You'll Learn

- **Variables**: Storing and updating data
- **Data Types**: Integers, strings, lists, dictionaries
- **Input/Output**: Getting user input and displaying results
- **Functions**: Organizing code into reusable blocks
- **Classes**: Object-oriented programming basics
- **Conditionals**: Making decisions in code
- **Loops**: Repeating actions (implicit in the game loop)
- **Data Structures**: Lists and dictionaries for complex data

## 🎯 Success Criteria

You'll know you've succeeded when:
- ✅ Your game variables update correctly
- ✅ User input changes the game state
- ✅ Calculations work properly
- ✅ The graphical display shows your data
- ✅ You understand how variables work in Python
- ✅ You can modify the game logic independently

Happy coding! 🎮
