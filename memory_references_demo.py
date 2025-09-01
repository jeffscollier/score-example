#!/usr/bin/env python3
"""
Memory References and Object Identity in Python
==============================================

This script demonstrates how Python handles memory references, aliasing,
and the differences between object identity (id()) and equality (==).
"""

import sys
from typing import Any, List, Dict


def demonstrate_memory_references():
    """
    Demonstrate how Python handles memory references and object identity.
    """
    print("=" * 70)
    print("MEMORY REFERENCES AND OBJECT IDENTITY")
    print("=" * 70)
    
    # Example 1: Immutable objects (integers, strings)
    print("\n1. IMMUTABLE OBJECTS (integers, strings):")
    print("-" * 45)
    
    a = 42
    b = 42
    c = a
    
    print(f"a = 42, b = 42, c = a")
    print(f"id(a): {id(a)}")
    print(f"id(b): {id(b)}")
    print(f"id(c): {id(c)}")
    print(f"a is b: {a is b}")  # True - Python optimizes small integers
    print(f"a is c: {a is c}")  # True - c points to same object as a
    print(f"a == b: {a == b}")  # True - values are equal
    
    # Example 2: Mutable objects (lists)
    print("\n2. MUTABLE OBJECTS (lists):")
    print("-" * 30)
    
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"list1 = [1, 2, 3]")
    print(f"list2 = [1, 2, 3]")
    print(f"list3 = list1")
    print(f"id(list1): {id(list1)}")
    print(f"id(list2): {id(list2)}")
    print(f"id(list3): {id(list3)}")
    print(f"list1 is list2: {list1 is list2}")  # False - different objects
    print(f"list1 is list3: {list1 is list3}")  # True - same object
    print(f"list1 == list2: {list1 == list2}")  # True - contents are equal
    
    # Example 3: Aliasing demonstration
    print("\n3. ALIASING DEMONSTRATION:")
    print("-" * 30)
    
    original_list = [10, 20, 30]
    alias_list = original_list
    
    print(f"original_list = [10, 20, 30]")
    print(f"alias_list = original_list")
    print(f"Before modification:")
    print(f"  original_list: {original_list}")
    print(f"  alias_list: {alias_list}")
    print(f"  id(original_list): {id(original_list)}")
    print(f"  id(alias_list): {id(alias_list)}")
    
    # Modify through one reference
    alias_list.append(40)
    
    print(f"After alias_list.append(40):")
    print(f"  original_list: {original_list}")  # Changed!
    print(f"  alias_list: {alias_list}")        # Changed!
    print(f"  id(original_list): {id(original_list)}")  # Same ID
    print(f"  id(alias_list): {id(alias_list)}")        # Same ID


def demonstrate_pseudocode_aliasing():
    """
    Show pseudocode examples of why a = b might create aliasing.
    """
    print("\n" + "=" * 70)
    print("PSEUDOCODE: WHY a = b MIGHT CREATE ALIASING")
    print("=" * 70)
    
    print("\nPSEUDOCODE EXAMPLE 1 - Immutable Objects:")
    print("-" * 45)
    print("""
    # Memory layout (simplified)
    Memory Address: 0x1000
    Object: Integer(42)
    
    # Python code:
    a = 42          # a points to object at 0x1000
    b = 42          # b points to same object at 0x1000 (Python optimization)
    c = a           # c points to same object at 0x1000
    
    # Result: a, b, c all point to the same memory location
    # But since integers are immutable, this is safe
    """)
    
    print("\nPSEUDOCODE EXAMPLE 2 - Mutable Objects:")
    print("-" * 45)
    print("""
    # Memory layout (simplified)
    Memory Address: 0x2000
    Object: List([1, 2, 3])
    
    Memory Address: 0x3000  
    Object: List([1, 2, 3])  # Different object, same contents
    
    # Python code:
    list1 = [1, 2, 3]        # list1 points to object at 0x2000
    list2 = [1, 2, 3]        # list2 points to object at 0x3000
    list3 = list1            # list3 points to object at 0x2000 (ALIAS!)
    
    # Result: list1 and list3 are aliases (same object)
    #         list2 is a different object with same contents
    """)
    
    print("\nPSEUDOCODE EXAMPLE 3 - Dangerous Aliasing:")
    print("-" * 45)
    print("""
    # Memory layout (simplified)
    Memory Address: 0x4000
    Object: List([10, 20, 30])
    
    # Python code:
    original = [10, 20, 30]  # original points to 0x4000
    backup = original        # backup points to 0x4000 (ALIAS!)
    
    # Later in code:
    backup.append(40)        # Modifies object at 0x4000
    
    # Result: Both original and backup now contain [10, 20, 30, 40]
    #         The "backup" wasn't really a backup!
    """)


def demonstrate_id_vs_equals():
    """
    Demonstrate the difference between id() (identity) and == (equality).
    """
    print("\n" + "=" * 70)
    print("id() vs == COMPARISON")
    print("=" * 70)
    
    # Example 1: Same object, same value
    print("\n1. SAME OBJECT, SAME VALUE:")
    print("-" * 30)
    a = [1, 2, 3]
    b = a
    
    print(f"a = [1, 2, 3]")
    print(f"b = a")
    print(f"a is b: {a is b}")      # True - same object
    print(f"a == b: {a == b}")      # True - same value
    print(f"id(a) == id(b): {id(a) == id(b)}")  # True - same memory address
    
    # Example 2: Different objects, same value
    print("\n2. DIFFERENT OBJECTS, SAME VALUE:")
    print("-" * 35)
    c = [1, 2, 3]
    d = [1, 2, 3]
    
    print(f"c = [1, 2, 3]")
    print(f"d = [1, 2, 3]")
    print(f"c is d: {c is d}")      # False - different objects
    print(f"c == d: {c == d}")      # True - same value
    print(f"id(c) == id(d): {id(c) == id(d)}")  # False - different memory addresses
    
    # Example 3: Different objects, different values
    print("\n3. DIFFERENT OBJECTS, DIFFERENT VALUES:")
    print("-" * 40)
    e = [1, 2, 3]
    f = [4, 5, 6]
    
    print(f"e = [1, 2, 3]")
    print(f"f = [4, 5, 6]")
    print(f"e is f: {e is f}")      # False - different objects
    print(f"e == f: {e == f}")      # False - different values
    print(f"id(e) == id(f): {id(e) == id(f)}")  # False - different memory addresses
    
    # Example 4: Mutable vs Immutable behavior
    print("\n4. MUTABLE vs IMMUTABLE BEHAVIOR:")
    print("-" * 35)
    
    # Immutable
    str1 = "hello"
    str2 = "hello"
    print(f"str1 = 'hello', str2 = 'hello'")
    print(f"str1 is str2: {str1 is str2}")  # True - string interning
    
    # Mutable
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"list1 = [1, 2, 3], list2 = [1, 2, 3]")
    print(f"list1 is list2: {list1 is list2}")  # False - always different objects


def demonstrate_copy_vs_reference():
    """
    Demonstrate the difference between copying and referencing.
    """
    print("\n" + "=" * 70)
    print("COPY vs REFERENCE")
    print("=" * 70)
    
    # Shallow copy example
    print("\n1. SHALLOW COPY:")
    print("-" * 20)
    original = [1, 2, [3, 4]]
    shallow_copy = original.copy()  # or list(original) or original[:]
    
    print(f"original = [1, 2, [3, 4]]")
    print(f"shallow_copy = original.copy()")
    print(f"original is shallow_copy: {original is shallow_copy}")  # False
    print(f"original == shallow_copy: {original == shallow_copy}")  # True
    
    # Modify the outer list
    original.append(5)
    print(f"After original.append(5):")
    print(f"  original: {original}")
    print(f"  shallow_copy: {shallow_copy}")
    
    # Modify the nested list
    original[2].append(6)
    print(f"After original[2].append(6):")
    print(f"  original: {original}")
    print(f"  shallow_copy: {shallow_copy}")  # Nested list is shared!
    
    # Deep copy example
    print("\n2. DEEP COPY:")
    print("-" * 15)
    import copy
    
    original2 = [1, 2, [3, 4]]
    deep_copy = copy.deepcopy(original2)
    
    print(f"original2 = [1, 2, [3, 4]]")
    print(f"deep_copy = copy.deepcopy(original2)")
    
    # Modify the nested list
    original2[2].append(7)
    print(f"After original2[2].append(7):")
    print(f"  original2: {original2}")
    print(f"  deep_copy: {deep_copy}")  # Nested list is independent!


def memory_references_quiz():
    """
    Interactive quiz on memory references and object identity.
    """
    print("\n" + "=" * 70)
    print("MEMORY REFERENCES QUIZ")
    print("=" * 70)
    
    questions = [
        {
            "question": "What will be the output of this code?\na = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)",
            "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "Error", "[4]"],
            "correct": 1,
            "explanation": "Since b is an alias of a (same object), modifying b also modifies a."
        },
        {
            "question": "What does 'a is b' check in Python?",
            "options": [
                "Whether a and b have the same value",
                "Whether a and b are the same object in memory",
                "Whether a and b are the same type",
                "Whether a and b are both mutable"
            ],
            "correct": 1,
            "explanation": "'is' checks object identity (same memory address), not value equality."
        },
        {
            "question": "What will be the result of this code?\nlist1 = [1, 2, 3]\nlist2 = [1, 2, 3]\nprint(list1 is list2)",
            "options": ["True", "False", "Error", "None"],
            "correct": 1,
            "explanation": "Even though the lists have the same contents, they are different objects in memory."
        },
        {
            "question": "What is 'aliasing' in Python?",
            "options": [
                "Creating a copy of an object",
                "Having multiple variables point to the same object",
                "Converting one type to another",
                "A special Python operator"
            ],
            "correct": 1,
            "explanation": "Aliasing occurs when multiple variables reference the same object in memory."
        },
        {
            "question": "What's the difference between shallow copy and deep copy?",
            "options": [
                "No difference, they're the same",
                "Shallow copy copies nested objects, deep copy doesn't",
                "Deep copy copies nested objects, shallow copy doesn't",
                "Shallow copy is faster but less accurate"
            ],
            "correct": 2,
            "explanation": "Deep copy creates independent copies of nested objects, while shallow copy shares nested objects."
        },
        {
            "question": "What will this code output?\na = 42\nb = 42\nprint(a is b)",
            "options": ["True", "False", "Error", "Depends on Python version"],
            "correct": 0,
            "explanation": "Python optimizes small integers by reusing the same object, so a and b point to the same 42."
        },
        {
            "question": "When should you use 'is' vs '==' for comparison?",
            "options": [
                "Always use 'is' for better performance",
                "Always use '==' for better readability",
                "Use 'is' for identity, '==' for value equality",
                "Use 'is' for mutable objects, '==' for immutable"
            ],
            "correct": 2,
            "explanation": "Use 'is' when you need to check if two variables point to the same object, '==' when you need to check if values are equal."
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(q["question"])
        print("\nOptions:")
        for j, option in enumerate(q["options"]):
            print(f"  {j + 1}. {option}")
        
        while True:
            try:
                answer = int(input("\nYour answer (1-4): ")) - 1
                if 0 <= answer < len(q["options"]):
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        if answer == q["correct"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {q['options'][q['correct']]}")
        
        print(f"Explanation: {q['explanation']}")
    
    print(f"\n" + "=" * 50)
    print(f"QUIZ RESULTS: {score}/{total_questions} correct")
    print("=" * 50)
    
    if score == total_questions:
        print("🎉 Perfect! You understand memory references well!")
    elif score >= total_questions * 0.8:
        print("👍 Great job! You have a solid understanding.")
    elif score >= total_questions * 0.6:
        print("📚 Good work! Review the explanations to improve.")
    else:
        print("📖 Keep studying! Memory references are tricky but important.")


def demonstrate_common_pitfalls():
    """
    Show common pitfalls related to memory references and aliasing.
    """
    print("\n" + "=" * 70)
    print("COMMON PITFALLS WITH MEMORY REFERENCES")
    print("=" * 70)
    
    print("\n1. PITFALL: Modifying a list through an alias:")
    print("-" * 45)
    print("""
    # Problematic code:
    def add_item_to_list(items, new_item):
        items.append(new_item)  # Modifies the original list!
        return items
    
    my_list = [1, 2, 3]
    result = add_item_to_list(my_list, 4)
    print(my_list)  # [1, 2, 3, 4] - original was modified!
    """)
    
    print("\n2. PITFALL: Default mutable arguments:")
    print("-" * 40)
    print("""
    # Problematic code:
    def add_to_list(item, target_list=[]):  # Default list is shared!
        target_list.append(item)
        return target_list
    
    # All calls share the same default list
    result1 = add_to_list(1)  # [1]
    result2 = add_to_list(2)  # [1, 2] - not [2]!
    """)
    
    print("\n3. PITFALL: Shallow copy with nested objects:")
    print("-" * 45)
    print("""
    # Problematic code:
    original = [1, 2, [3, 4]]
    copy_list = original.copy()  # Shallow copy
    
    copy_list[2].append(5)  # Modifies nested list in original too!
    print(original)  # [1, 2, [3, 4, 5]] - original was modified!
    """)


def main():
    """
    Main function to run all demonstrations.
    """
    print("Welcome to the Python Memory References Demonstration!")
    print("This script will teach you about object identity, aliasing, and memory management.")
    
    # Run all demonstrations
    demonstrate_memory_references()
    demonstrate_pseudocode_aliasing()
    demonstrate_id_vs_equals()
    demonstrate_copy_vs_reference()
    demonstrate_common_pitfalls()
    
    # Ask if user wants to take the quiz
    print("\n" + "=" * 70)
    response = input("Would you like to take the memory references quiz? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        memory_references_quiz()
    else:
        print("Thanks for exploring Python's memory references! 🧠")
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("• 'is' checks object identity (same memory address)")
    print("• '==' checks value equality (same contents)")
    print("• Aliasing occurs when multiple variables point to the same object")
    print("• Mutable objects can be modified through any alias")
    print("• Shallow copy shares nested objects, deep copy creates independent copies")
    print("• Python optimizes small integers and strings (interning)")
    print("• Be careful with default mutable arguments and function parameters")


if __name__ == "__main__":
    main()
