#!/usr/bin/env python3
"""
Simple Hello World Python Script
A basic demonstration of Python programming fundamentals.
"""

def greet(name="World"):
    """
    Greet someone with a personalized message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def main():
    """Main function to run the hello world program."""
    print("=" * 40)
    print("Welcome to Python Hello World!")
    print("=" * 40)
    
    # Get user input
    name = input("What's your name? ").strip()
    
    # Greet the user
    if name:
        message = greet(name)
    else:
        message = greet()
    
    print(f"\n{message}")
    print("Nice to meet you! 👋")
    print("=" * 40)

if __name__ == "__main__":
    main()
