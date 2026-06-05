#Carlos Salgado
# Student ID:5001363
# date: 5/20/2026
# Program Description: This program builds a
# shopping list, categorizes each item by price,
# calculates the total cost, and saves the results
# to a text file.


# Function to categorize an item based on its price
def get_category(price):
    if price < 10:
        return "Cheap"
    elif price < 20:
        return "Moderate"
    else:
        return "Expensive"


# Function to calculate the total cost of all items
def calculate_total(shopping_list):
    total = 0
    for item in shopping_list:
        total = total + shopping_list[item]["price"]
    return total


# Ask how many items the user wants to add
num_items = int(input("How many items? "))

# Dictionary to store all shopping list items
shopping_list = {}

# Loop through each item and collect its info
for i in range(num_items):
    print("\nItem", i + 1)

    # Get the item name and price
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))

    # Get the category using the function
    category = get_category(price)

    # Save the item in the dictionary under its name
    shopping_list[name] = {
        "price": price,
        "category": category
    }


# ----- Display the Results -----
print("\n----- Shopping List -----")
for name in shopping_list:
    info = shopping_list[name]
    print("\nItem:", name)
    print("Price: $", round(info["price"], 2))
    print("Category:", info["category"])

# Calculate and display the total cost
total_cost = calculate_total(shopping_list)
print("\nTotal Cost: $", round(total_cost, 2))


# ----- Save Results to a File -----
file = open("shopping_list.txt", "w")
file.write("----- Shopping List -----\n")
for name in shopping_list:
    info = shopping_list[name]
    file.write("\nItem: " + name + "\n")
    file.write("Price: $" + str(round(info["price"], 2)) + "\n")
    file.write("Category: " + info["category"] + "\n")
file.write("\nTotal Cost: $" + str(round(total_cost, 2)) + "\n")
file.close()

print("\nShopping list saved to shopping_list.txt")

# Answer the reflection questions:
# 1. Which part of this program was the easiest to write, and why?
"""The easiest part was the function that picks the category. It is just an if/elif/else with three checks, so the logic is short and clear."""
# 2. Which part was the most challenging, and how did you solve it?
"""The hardest part was getting the dictionary set up so each item held both a price and a category inside it. I figured it out by printing the dictionary after the loop to see what was actually in there."""
# 3. Why did you use a dictionary instead of separate variables?
"""I used a dictionary because I needed to keep the price and the category together for each item. Separate variables would get messy fast once you have more than a couple items."""
# 4. Why is a loop necessary in this program?
"""A loop is needed because I do not know how many items the user will enter. The loop runs once per item so I do not have to copy the input code over and over."""
# 5. How does your function determine item categories?
"""The function compares the price to two numbers. Under 10 is Cheap, under 20 is Moderate, and anything else is Expensive."""

# Answer the reflection questions:
# 6. One thing the AI solution did differently than my program was:
"""The AI built the report text once in a function and then used it for both the screen and the file. My program had two loops that did almost the same thing, once for printing and once for writing."""
# 7. One part of my original code I understand better now is:
"""I understand the nested dictionary better now. The item name is the key, and the value is another dictionary holding the price and category. That lets me pull both out together when I loop through the items."""
# 8. One part of the AI code I do not fully understand is:
"""The line with open("shopping_list.txt", "w") as file: is new to me. I am used to writing file = open(...) and then file.close() at the end. The with version closes the file by itself, and I am still getting used to writing it that way."""
# 9. Where would you start debugging and why?
"""I would start at the price input. float(input()) will crash if the user types something that is not a number, and the rest of the program needs a valid number for the category function and the total."""
# 10. Which approach would you keep and why?
"""I would keep the AI approach. Building the report once means I only have to change one spot if I want the output to look different later. The with open() part is also safer because the file always gets closed."""