#!/usr/bin/env python3
"""
Dynamic Typing vs Static Typing Demonstration
============================================

This script demonstrates Python's dynamic typing system and contrasts it
with static typing languages like Java, C++, or TypeScript.
"""

import sys
from typing import Any, Union, Optional


def demonstrate_dynamic_typing():
    """
    Demonstrate Python's dynamic typing with variable reassignment examples.
    """
    print("=" * 60)
    print("PYTHON DYNAMIC TYPING DEMONSTRATION")
    print("=" * 60)
    
    # Example 1: Variable can change type during runtime
    print("\n1. VARIABLE TYPE REASSIGNMENT:")
    print("-" * 30)
    
    my_variable = 42
    print(f"Initial value: {my_variable} (type: {type(my_variable).__name__})")
    
    my_variable = "Hello, World!"
    print(f"After reassignment: {my_variable} (type: {type(my_variable).__name__})")
    
    my_variable = [1, 2, 3, 4, 5]
    print(f"After another reassignment: {my_variable} (type: {type(my_variable).__name__})")
    
    my_variable = {"name": "Python", "typing": "dynamic"}
    print(f"After final reassignment: {my_variable} (type: {type(my_variable).__name__})")
    
    # Example 2: Function parameters can accept any type
    print("\n2. FUNCTION PARAMETER FLEXIBILITY:")
    print("-" * 35)
    
    def process_data(data):
        """This function can accept any type of data."""
        print(f"Processing: {data} (type: {type(data).__name__})")
        if isinstance(data, (int, float)):
            return data * 2
        elif isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return len(data)
        else:
            return "Unknown type"
    
    # Test with different types
    test_values = [42, "hello", [1, 2, 3], 3.14, {"key": "value"}]
    for value in test_values:
        result = process_data(value)
        print(f"  Input: {value} -> Output: {result}")
    
    # Example 3: Duck typing - "If it walks like a duck and quacks like a duck..."
    print("\n3. DUCK TYPING EXAMPLE:")
    print("-" * 25)
    
    class Duck:
        def quack(self):
            return "Quack!"
        
        def walk(self):
            return "Waddle waddle"
    
    class Person:
        def quack(self):
            return "I'm pretending to be a duck!"
        
        def walk(self):
            return "Walking like a duck"
    
    def make_duck_sounds(animal):
        """This function works with any object that has quack() and walk() methods."""
        print(f"Sound: {animal.quack()}")
        print(f"Movement: {animal.walk()}")
    
    duck = Duck()
    person = Person()
    
    print("Real duck:")
    make_duck_sounds(duck)
    
    print("\nPerson pretending to be a duck:")
    make_duck_sounds(person)


def demonstrate_static_typing_concepts():
    """
    Show how static typing would work (using Python's type hints for comparison).
    """
    print("\n" + "=" * 60)
    print("STATIC TYPING CONCEPTS (Python Type Hints)")
    print("=" * 60)
    
    # Example with type hints
    def add_numbers(a: int, b: int) -> int:
        """Function with explicit type hints."""
        return a + b
    
    def process_string(text: str) -> str:
        """Function that expects a string."""
        return text.upper()
    
    # This would work fine
    result1 = add_numbers(5, 3)
    print(f"add_numbers(5, 3) = {result1}")
    
    # This would also work (Python ignores type hints at runtime)
    result2 = add_numbers("5", "3")  # String concatenation!
    print(f"add_numbers('5', '3') = {result2}")
    
    print("\nNote: Python's type hints are optional and don't enforce types at runtime!")
    print("In true static languages, the second call would cause a compile-time error.")


def type_inference_quiz():
    """
    Interactive quiz on type inference implications.
    """
    print("\n" + "=" * 60)
    print("TYPE INFERENCE QUIZ")
    print("=" * 60)
    
    questions = [
        {
            "question": "What will be the type of 'x' after this code runs?\nx = 42\nx = 'hello'\nprint(type(x))",
            "options": ["int", "str", "Union[int, str]", "Any"],
            "correct": 1,
            "explanation": "In Python, variables don't have fixed types. The type is determined by the current value."
        },
        {
            "question": "In a static language like Java, what happens if you try to assign a string to an int variable?",
            "options": ["Runtime error", "Compile-time error", "Automatic conversion", "Works fine"],
            "correct": 1,
            "explanation": "Static languages check types at compile time and prevent type mismatches."
        },
        {
            "question": "What is 'duck typing' in Python?",
            "options": [
                "A way to create duck objects",
                "Using type hints for waterfowl",
                "Objects are judged by their behavior, not their type",
                "A special typing module for animals"
            ],
            "correct": 2,
            "explanation": "Duck typing means 'if it walks like a duck and quacks like a duck, it's a duck' - behavior matters more than explicit type."
        },
        {
            "question": "What's the main advantage of dynamic typing?",
            "options": [
                "Better performance",
                "More flexibility and less boilerplate",
                "Fewer bugs",
                "Better IDE support"
            ],
            "correct": 1,
            "explanation": "Dynamic typing offers flexibility and requires less code, but can lead to runtime errors that static typing would catch earlier."
        },
        {
            "question": "What's the main disadvantage of dynamic typing?",
            "options": [
                "Slower execution",
                "Runtime type errors that could be caught at compile time",
                "More memory usage",
                "Harder to read"
            ],
            "correct": 1,
            "explanation": "Type errors that would be caught at compile time in static languages only surface at runtime in dynamic languages."
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
    
    print(f"\n" + "=" * 40)
    print(f"QUIZ RESULTS: {score}/{total_questions} correct")
    print("=" * 40)
    
    if score == total_questions:
        print("🎉 Perfect! You understand dynamic typing well!")
    elif score >= total_questions * 0.8:
        print("👍 Great job! You have a good understanding.")
    elif score >= total_questions * 0.6:
        print("📚 Not bad! Review the explanations to improve.")
    else:
        print("📖 Keep studying! Dynamic typing concepts take time to master.")


def demonstrate_type_related_functions():
    """
    Show various type-related functions and their behavior.
    """
    print("\n" + "=" * 60)
    print("PYTHON TYPE-RELATED FUNCTIONS")
    print("=" * 60)
    
    # Demonstrate type() function
    print("\n1. type() function:")
    print("-" * 20)
    values = [42, 3.14, "hello", [1, 2, 3], {"key": "value"}, True, None]
    for value in values:
        print(f"  {repr(value):>12} -> {type(value).__name__}")
    
    # Demonstrate isinstance() function
    print("\n2. isinstance() function:")
    print("-" * 25)
    test_value = [1, 2, 3]
    print(f"isinstance({test_value}, list): {isinstance(test_value, list)}")
    print(f"isinstance({test_value}, str): {isinstance(test_value, str)}")
    print(f"isinstance({test_value}, (list, tuple)): {isinstance(test_value, (list, tuple))}")
    
    # Demonstrate hasattr() for duck typing
    print("\n3. hasattr() for duck typing:")
    print("-" * 30)
    
    class Car:
        def drive(self):
            return "Vroom!"
    
    class Bicycle:
        def ride(self):
            return "Pedal pedal!"
    
    def make_it_go(vehicle):
        if hasattr(vehicle, 'drive'):
            return vehicle.drive()
        elif hasattr(vehicle, 'ride'):
            return vehicle.ride()
        else:
            return "I don't know how to make this go!"
    
    car = Car()
    bike = Bicycle()
    
    print(f"Car: {make_it_go(car)}")
    print(f"Bicycle: {make_it_go(bike)}")


def main():
    """
    Main function to run all demonstrations.
    """
    print("Welcome to the Python Dynamic Typing Demonstration!")
    print("This script will show you the nuances of Python's dynamic typing system.")
    
    # Run all demonstrations
    demonstrate_dynamic_typing()
    demonstrate_static_typing_concepts()
    demonstrate_type_related_functions()
    
    # Ask if user wants to take the quiz
    print("\n" + "=" * 60)
    response = input("Would you like to take the type inference quiz? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        type_inference_quiz()
    else:
        print("Thanks for exploring Python's dynamic typing! 🐍")
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("• Python variables don't have fixed types - they can change type during runtime")
    print("• Dynamic typing offers flexibility but can lead to runtime errors")
    print("• Duck typing allows objects to be used based on their behavior, not their type")
    print("• Type hints in Python are optional and don't enforce types at runtime")
    print("• Static languages catch type errors at compile time; dynamic languages at runtime")


if __name__ == "__main__":
    main()
