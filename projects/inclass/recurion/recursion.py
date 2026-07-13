#Carlos Salgado
# Student ID:5001363
# date: 7/13/2026
# Program Description: This program demonstrates recursion through
#   countdown functions and a reverse spell function. Includes
#   user input and fun messages/emojis.

def magic_countdown(n):
    """Challenge 1: Countdown with fun messages and emojis"""
    if n == 0:  # Base case - stop when we reach 0
        print("🚀 Blast Off! 🚀")
        return
    print(f"{n} 🎉 Get ready!")
    magic_countdown(n - 1)  # Recursive case - call itself with n-1

def reverse_spell(word, index=0):
    """Challenge 3: Print a word in reverse, one character per line"""
    if index == len(word):  # Base case - reached end of word
        return
    # Recursively go to the end first
    reverse_spell(word, index + 1)
    # Then print on the way back (reverse order)
    print(word[index])  # Prints after recursive call returns

def main():
    print("Starting magic countdown...")
    
    # Challenge 2: Ask user for starting number
    try:
        start = int(input("Enter a starting number for countdown: "))
        if start < 0:
            print("Please enter a positive number!")
            return
        magic_countdown(start)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return
    
    # Challenge 3: Reverse spell (Optional Extra Credit)
    print("\n--- Bonus: Reverse Spell ---")
    word = input("Enter a word to spell backwards: ")
    print(f"Spelling '{word}' in reverse:")
    reverse_spell(word)

if __name__ == "__main__":
    main()

# ─── Reflection Questions ────────────────────────────────────────────────────

# 1. What is recursion in your own words?
"""Recursion is when a function calls itself to break down a problem into 
smaller pieces until it reaches a simple case it can solve directly."""

# 2. What is the base case in your program and why is it important?
"""The base case is when n == 0 in magic_countdown() and when index == len(word) 
in reverse_spell(). It's important because it tells the function when to stop 
calling itself, preventing infinite loops that would crash the program."""

# 3. What is the recursive pattern in your function?
"""In magic_countdown(): Print the current number, then call itself with n-1.
In reverse_spell(): Call itself with index+1 first, then print on the way back.
Both follow the pattern: check base case, do work, call itself with modified input."""

# 4. What could go wrong if your program did not have a base case?
"""The function would call itself forever (infinite recursion) until Python 
runs out of memory and crashes with a RecursionError: maximum recursion depth exceeded."""

# ─── AI Comparison ───────────────────────────────────────────────────────────

# 1. What similarities did you notice?
"""Both used the same basic structure: if statement for base case, recursive call 
with modified parameter, and similar logic for counting down."""

# 2. What differences did you notice?
"""The AI version was cleaner and more focused on the core recursion concept. 
I added extra features like emojis, user input validation, and error handling 
which made it more complex but also more user-friendly."""

# 3. Which parts of the AI solution were helpful?
"""The AI's simple, clean approach made the recursive logic easier to understand. 
It also handled the reverse_spell function more elegantly by focusing just on 
the recursion without extra print statements. The AI code was easier to read."""

# 4. What changes did you make to make the program your own?
"""I added emojis and fun messages for each countdown number, user input for 
the starting number, input validation with try-except, and extra comments 
explaining how recursion works. The AI kept it simpler which was actually better 
for learning."""