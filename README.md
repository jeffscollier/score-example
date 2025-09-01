# Python Game Development Learning Repository

## 🎮 Overview

This repository is designed to teach Python programming concepts through interactive game development. It focuses on **variable management**, **user input handling**, and **real-time graphics** using Pygame.

## 📁 Repository Structure

```
score-example/
├── README.md                           # This file
├── game_ui_demo.py                     # Complete working example (class-based)
├── game_score_demo template.py         # Student template (procedural)
├── student_game_template.py            # Original student template (class-based)
├── setup_game_demo.py                  # Setup script for pygame installation
├── requirements.txt                    # Python dependencies
└── student_learning_guide.md           # Additional learning resources
```

## 🎯 Learning Objectives

Students will learn:
- **Variable Declaration & Initialization**
- **User Input Processing**
- **Real-time Variable Updates**
- **Graphics Programming Basics**
- **Procedural vs Object-Oriented Programming**
- **Python's Dynamic Typing System**
- **Memory References and Aliasing**

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation
1. Clone or download this repository
2. Install pygame:
   ```bash
   pip install pygame
   ```
   Or run the setup script:
   ```bash
   python setup_game_demo.py
   ```

### Running the Examples
```bash
# Run the complete working example
python game_ui_demo.py

# Run the student template (will need completion)
python "game_score_demo template.py"
```

## 📚 Student Template: `game_score_demo template.py`

### What's Missing?
The student template has **intentionally removed** key components that students must implement:

#### 🔴 **Critical Missing Elements:**
1. **Game Variables** (Line 48)
   - `player_health`, `max_health`, `score`, `status`, `power_ups`, `level`
   - **Impact**: Game won't run without these

2. **Input Handling Logic** (Lines 212-218)
   - Health increase/decrease logic
   - Score modification logic
   - **Impact**: Keys won't do anything

3. **Reset Function Logic** (Lines 239-244)
   - Variable reset assignments
   - **Impact**: Reset button won't work

#### 🟡 **Partial Elements:**
- Display functions are complete but depend on missing variables
- Animation system is intact
- Graphics framework is fully functional

### 🎓 Learning Progression

#### **Level 1: Basic Variables**
```python
# Students must add:
player_health = 100
max_health = 100
score = 0
status = "Alive"
power_ups = []
level = 1
```

#### **Level 2: Input Processing**
```python
# Students must implement:
if event.key == pygame.K_h:  # Heal
    player_health = min(max_health, player_health + 10)
elif event.key == pygame.K_d:  # Damage
    player_health = max(0, player_health - 10)
elif event.key == pygame.K_s:  # Score
    score += 100
    score_animation = 10
```

#### **Level 3: Game State Management**
```python
# Students must complete:
def reset_game():
    global player_health, score, status, power_ups, level
    player_health = 100
    score = 0
    status = "Alive"
    power_ups = []
    level = 1
```

## 🎮 Game Controls

Once completed, the game supports:
- **H** - Heal (+10 health)
- **D** - Take Damage (-10 health)
- **S** - Add Score (+100 points)
- **P** - Add Random Power-up
- **R** - Reset Game
- **ESC** - Quit

## 🧠 Advanced Learning: Cursor AI Prompts

Use these prompts with Cursor AI to deepen your understanding:

### 1. Dynamic Typing Exploration
```
"Using a python script, explain Python's dynamic typing nuances vs. static languages; use a variable reassignment example and quiz me on type inference implications"
```

**What you'll learn:**
- How Python variables can change types
- Type inference vs explicit typing
- Runtime vs compile-time type checking
- Memory implications of dynamic typing

### 2. Memory References & Aliasing
```
"Teach me about memory references: Show with pseudocode why a = b might alias; quiz on id() vs == in mutable types."
```

**What you'll learn:**
- Object identity vs equality
- Shallow vs deep copying
- Mutable vs immutable types
- Memory address concepts with `id()`

## 🔍 Template Analysis

### **STUDENT TEMPLATE Sections:**

1. **GAME VARIABLES SECTION** (Lines 41-53)
   - Where core game data is defined
   - Students learn variable initialization

2. **USER INPUT SECTION** (Lines 200-227)
   - Where keyboard input is processed
   - Students learn conditional logic and variable modification

3. **GAME STATE RESET SECTION** (Lines 229-245)
   - Where variables are restored to initial values
   - Students learn state management

4. **SCORE DISPLAY SECTION** (Lines 134-157)
   - Where variables are read and displayed
   - Students learn data presentation

5. **GAME STATE UPDATE SECTION** (Lines 190-198)
   - Where variables change automatically
   - Students learn time-based programming

## 🎯 Expected Learning Outcomes

After completing the template, students will understand:

- **Variable Lifecycle**: Declaration → Modification → Display → Reset
- **User Interaction**: How input events trigger variable changes
- **Real-time Programming**: How variables update continuously
- **Graphics Integration**: How data drives visual elements
- **Error Handling**: What happens when variables are undefined

## 🐛 Common Student Mistakes

1. **Missing Global Declarations**
   ```python
   # Wrong:
   def handle_input(event):
       score += 100  # Error: local variable referenced before assignment
   
   # Correct:
   def handle_input(event):
       global score
       score += 100
   ```

2. **Undefined Variables**
   ```python
   # Wrong:
   # Missing: player_health = 100
   draw_health_bar(50, 80, 300, 40, player_health, max_health)  # Error
   ```

3. **Incomplete Reset Logic**
   ```python
   # Wrong:
   def reset_game():
       # Missing variable assignments
   
   # Correct:
   def reset_game():
       global player_health, score, status
       player_health = 100
       score = 0
       status = "Alive"
   ```

## 🎓 Assessment Ideas

### **Beginner Level:**
- Can the game run without errors?
- Do the basic controls (H, D, S) work?
- Does the reset function work?

### **Intermediate Level:**
- Are variables properly managed with `global`?
- Does the game handle edge cases (health < 0)?
- Are animations working correctly?

### **Advanced Level:**
- Can students add new features (new keys, new variables)?
- Do they understand the relationship between variables and display?
- Can they explain the procedural programming approach?

## 📖 Additional Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Global Variables](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Game Programming Patterns](https://gameprogrammingpatterns.com/)

## 🤝 Contributing

This is a teaching repository. Feel free to:
- Add more learning exercises
- Improve the template structure
- Create additional examples
- Enhance the documentation


---

**Happy Learning! 🎮🐍**
