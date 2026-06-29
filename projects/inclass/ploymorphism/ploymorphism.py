#Carlos Salgado
# Student ID:5001363
# date: 6/29/2026
# Program Description: This program demonstrates polymorphism using
#   a base Animal class and several subclasses. It also shows
#   simple method "overloading" with default parameters and
#   duck typing with a Robot and Alien class.
class Animal:
   # Base class — gives a generic sound
   def speak(self):
       return "..."
class Dog(Animal):
   # Overrides speak() with a dog sound
   def speak(self):
       return "Woof!"
class Cat(Animal):
   # Overrides speak() with a cat sound
   def speak(self):
       return "Meow!"
class Bird(Animal):
   # Modification: new animal with its own sound
   def speak(self):
       return "Tweet!"

 # Create one object of each animal
dog = Dog()
cat = Cat()
bird = Bird()  

print("----- Part 1: Polymorphism with Method Overriding -----")
print("Dog says:", dog.speak())
print("Cat says:", cat.speak())
print("Bird says:", bird.speak())

# ----- Part 2: Simple "Overloading" with Default Parameters -----
def repeat_sound(animal, times=1):
   for i in range(times):
       print(animal.speak())

print("\n----- Part 2: Repeat Sound with Default Parameters -----")
print("Dog once (default):")
repeat_sound(dog)
repeat_sound(cat, times=3)


# ----- Part 3: Duck Typing -----
class Robot:
   def speak(self):
       return "Beep boop!"
class Alien:
   def speak(self):
       return "Glorp zorp!"

def make_animal_speak(thing):
    print(thing.speak())

robot = Robot()
alien = Alien()

print("\n----- Part 3: Duck Typing -----")
print("Dog:")
make_animal_speak(dog)
print("Cat:")
make_animal_speak(cat)
print("Robot:")
make_animal_speak(robot)
print("Bird:")
make_animal_speak(bird)
print("Alien:")
make_animal_speak(alien)

# ============================================
# Reflection Questions

# 1. How does overriding create polymorphism in this project?
"""Each subclass (Dog, Cat, Bird) has its own version of speak(). When we call speak() on any of them, Python runs the right version for that object. Same method name, different behavior."""

# 2. Why does Python use default parameters instead of true method overloading?
"""Python only allows one method with a given name per class. If you define it twice, the second one just replaces the first. Default parameters let us handle the "called with fewer arguments" case inside one function."""

# 3. Explain duck typing using your own example.
"""Robot and Alien are not Animal subclasses at all, but they both have speak(). make_animal_speak() doesn't check the type — it just calls speak() and trusts it's there. "If it quacks like a duck, treat it like a duck." """
# ============================================


# ─── AI Comparison ──────────────────────────────────────────────────────────

# 1. What differences do you notice between your code and the AI-generated code?
"""The AI added more classes and used loops to call speak() on a list of animals. My version calls each one manually."""

# 2. What is one thing the AI did well in its solution?
"""It used a list and a for loop to iterate over all animals, which is cleaner than printing each one separately."""

# 3. What is one part of your code that you understand better than the AI solution?
"""I understand my repeat_sound() function better because I wrote the logic myself and know exactly why default parameters are used."""

# 4. Did the AI solution use Polymorphism correctly? Explain.
"""Yes. It called the same speak() method on different object types and each returned its own output — that's exactly what polymorphism means."""

# 5. Which version of the code (yours or AI) is easier to understand, and why?
"""Mine is easier to follow because it's step-by-step and doesn't have extra abstractions. The AI version is more compact but harder to read at first."""

# 6. What is one improvement you could make to your code after comparing it with AI?
"""Use a list to store all the animals and loop through them instead of printing each one individually."""