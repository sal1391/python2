# Carlos Salgado
# Student ID:5001363
# date: 5/26/2026
# Program Description: This program creates a Pet
# class with a class attribute, constructor, and
# methods. It demonstrates the difference between
# class and object, and how class attributes
# increase when new objects are created.

# Define the Pet Class

class Pet:
    # Class attribute - counts all pets
    total_pets = 0

    # Constructor - runs when a new Pet is created
    def __init__(self, name, pet_type, tasks):
        self.name = name
        self.pet_type = pet_type
        self.tasks = tasks
        Pet.total_pets = Pet.total_pets + 1

    # Method to add a task
    def add_task(self, task):
        self.tasks.append(task)

# Create first pet
pet1 = Pet("Mike", "Dog", [])

# Create second pet
pet2 = Pet("Kitty", "Cat", [])


# Add a task to pet1
pet1.add_task("roll-over")

# Add a task to pet2
pet2.add_task("paw")

# Add a nickname to pet1
pet1.nickname = "Mike the Magnificent"

# Add a nickname to pet2
pet2.nickname = "Kitty the Cute"

# Print Results
print("Total Pets:", Pet.total_pets)

print("Pet 1:")
print("Name:", pet1.name)
print("Type:", pet1.pet_type)
print("Tasks:", pet1.tasks)
print("Nickname:", pet1.nickname)
print()

print("Pet 2:")
print("Name:", pet2.name)
print("Type:", pet2.pet_type)
print("Tasks:", pet2.tasks)
print("Nickname:", pet2.nickname)
print()

# Answer the reflection questions:

# 1. Difference between class and object
"""
A class is like a template. An object is what you create from that template. 
Pet is the class, and pet1 and pet2 are the objects I made from it.
"""

# 2. Why total_pets increases
"""
Every time I create a new Pet, the code Pet.total_pets = Pet.total_pets + 1 
runs automatically. That adds 1 to the counter. So it goes 0, then 1, then 2.
"""

# 3. Why use a list
"""
A list lets me store multiple tasks. If I used a single variable, I could 
only hold one task. With a list, I can add as many as I want.
"""

# 4. What isinstance() does
"""
isinstance() checks if something is an object of a certain class. If I do 
isinstance(pet1, Pet), it returns True because pet1 is a Pet.
"""

# 5. Purpose of __init__
"""
__init__ sets up a new object when you create it. It gives the object its 
name, type, and tasks. It also adds 1 to total_pets to keep count of how 
many pets I made.
"""

# 6. Difference from AI:
""" My program uses my own ideas and understanding,
 while AI helps give examples, suggestions,
 and explanations
 ."""

# 7. AI Strength:
"""AI can quickly generate code, explain concepts,
# and help fix errors.
# """

# 8. Your Strength:
"""My strength is understanding the assignment,
# making decisions, and learning how the code works.
# """

# 9. What You Don’t Understand:
"""I still need more practice with class attributes,
# constructors, and object methods.
# """

# 10. Which Version is Better:
"""I think my version is better for me because
 I understand it more clearly and it matches
 my coding style.
 """

