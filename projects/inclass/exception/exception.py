#Carlos Salgado
# Student ID:5001363
# date: 6/29/2026
# Date: 07/06/2026
# Program Description: A snack shop simulation that demonstrates custom exceptions,
#                      try/except error handling, LBYL vs EAFP strategies, and order totals.

# --- Custom Exception ---
class TooManySnacksError(Exception):
    pass


# --- Data (Menu) ---
snacks = {
    "chips": 1.50,
    "cookies": 2.00,
    "pretzels": 1.75,
    "water": 1.00
}


print("Welcome to the Snack Shop")
print("Menu:")

for item, price in snacks.items():
    print(f"{item}: ${price:.2f}")

# --- Safe Number Input (try/except) ---
try:
    qty = int(input("How many snacks do you want? "))

    # --- Challenges 1 & 2 ---
    if qty > 10:
        raise TooManySnacksError("You cannot order more than 10 snacks")

    # --- LBYL vs EAFP Snack Choice ---
    choice = input("Choose a snack: ").lower()

    if choice in snacks:
        print(f"{choice} is available")
    else:
        print("Snack not found")

    try:
        price = snacks[choice]

    except KeyError:
        print("EAFP: Invalid snack. Defaulting to chips.")
        choice = "chips"
        price = snacks[choice]

    total = price * qty

    # --- Checkout & Messages ---
    print(f"You selected {choice}.")
    print(f"Total cost: ${total:.2f}")

except ValueError:
    print("Invalid input. Please enter a number for quantity.")
except TooManySnacksError as e:
    print(e)
finally:
    print("Thank you for visiting the Snack Shop!")


# ─── Reflection Questions ────────────────────────────────────────────────────

# 1. What is an exception and how is it different from a syntax error?
"""An exception is a runtime error that happens while the program is running,
like entering a letter when a number is expected or ordering too many snacks.
A syntax error is caught before the program runs at all — it means the code
is written incorrectly and Python cannot even read it."""

# 2. Show where you used LBYL and where you used EAFP. Why might you choose one over the other?
"""LBYL: 'if choice in snacks:' checks before accessing the dictionary.
EAFP: 'try: price = snacks[choice] except KeyError:' just tries it and handles the failure.
LBYL is clearer when the check is simple and cheap. EAFP is better when a
failed attempt is rare and you want the code to stay clean."""

# 3. What does finally do in your program? Why is it useful?
"""finally always runs whether an exception occurred or not. Here it prints the
goodbye message no matter what the user did. It is useful for cleanup code
that must always execute, like closing a file or ending a session."""

# 4. Why did you create a custom exception? How did it help your program?
"""TooManySnacksError gives a meaningful name to a business rule violation.
It separates a rule erroron from a generic Python error,
making it easy to catch and handle just that specific case without catching
everything."""


# ─── AI Comparison ───────────────────────────────────────────────────────────

# 1. What similarities did you notice?
"""The AI also used a dictionary for the menu, try/except for input validation,
and a finally block for the closing message."""

# 2. What differences did you notice?
"""The AI used a while loop to keep asking until valid input was given. My version
exits with an error message on bad input instead of retrying."""

# 3. Which parts of the AI solution were helpful?
"""Seeing how the AI nested the EAFP try block inside the outer try block helped
me understand that exception handling can be layered cleanly."""

# 4. What changes did you make to make the program your own?
"""I added TooManySnacksError as a custom exception, added the LBYL check before
the EAFP block, added water to the menu, and calculated the total cost."""