#Carlos Salgado
# Student ID:5001363
# date: 6/205/2026
# Program Description: This program defines a ConcertTicket class with attributes and methods to manage concert tickets. 
# It demonstrates creating ticket objects, modifying them with methods, and using class attributes.

# ---- Part 1: Vocabulary ----

# 1. What is a class?
'''A class is a blueprint for creating objects. It defines what attributes (data) and methods (actions) an object will have'''

#2. What is an object?
'''An object is one specific instance created from a class.  Each object has its own copy of the class's attributes.'''

# 3. What does self represent?
'''self refers to the current object. It lets methods access
and update that object's own attributes.'''


# ---- Part 2: Create a Class ----

class ConcertTicket:
    # Class attribute — shared by all tickets
    service_fee = 5

    def __init__(self, event_name, customer_name, price, extras=None):
        self.event_name = event_name
        self.customer_name = customer_name
        self.price = price

        if extras is None:
            self.extras = []
        else:
            self.extras = extras

    # ---- Part 3: Methods ----

    def add_extra(self, item):
        self.extras.append(item)

    def apply_discount(self, percent):
        discount = self.price * (percent / 100.0)
        self.price = self.price - discount

    def print_details(self):
        print("--- Ticket ---")
        print("Event:    ", self.event_name)
        print("Customer: ", self.customer_name)
        print("Price:    $" + str(self.price))
        print("Extras:   ", self.extras)
        print("Service Fee: $" + str(ConcertTicket.service_fee))
        print("")


# ---- Create 2 ticket objects ----
ticket1 = ConcertTicket("Rock Fest", "Alice", 80)
ticket2 = ConcertTicket("Jazz Night", "Bob", 50)

print("=== Initial Tickets ===")
ticket1.print_details()
ticket2.print_details()

# ---- Written Response (Part 2) ----
# Why use None instead of [] for extras?
'''If we used [] as the default, Python creates ONE list shared across all tickets. Every ticket would accidentally share extras.
Using None and making a new list inside __init__ keeps each ticket's extras separate'''


# ---- Test Methods (Part 3) ----
ticket1.add_extra("T-Shirt")
ticket1.add_extra("Backstage Pass")
ticket2.apply_discount(10)   # 10% off

print("=== After Methods ===")
ticket1.print_details()
ticket2.print_details()

# ---- Written Response (Part 3) ----
# What is one benefit of using methods instead of changing attributes directly?
'''Methods let you add logic instead of just setting a value. This keeps the code organized
and prevents mistakes from doing the math wrong every time'''


# ---- Part 4: Class Attribute ----

print("=== Service Fee ===")
print("Via class:  $" + str(ConcertTicket.service_fee))
print("Via object: $" + str(ticket1.service_fee))


ConcertTicket.service_fee = 10
print("After change:")
print("ticket1 fee: $" + str(ticket1.service_fee))
print("ticket2 fee: $" + str(ticket2.service_fee))
print("")

# ---- Written Response (Part 4) ----
#Why do both objects show the updated value?
'''Service_fee belongs to the class, not to each object. Both ticket1 and ticket2 look it up from the same class,
so when it changes there, both see the new value'''


# ---- Part 5: Extension ----

ticket3 = ConcertTicket("Pop Showcase", "Carol", 65)
ticket3.add_extra("Meet & Greet")

print("=== All Tickets ===")
ticket1.print_details()
ticket2.print_details()
ticket3.print_details()


# ---- Reflection Questions ----

# 1. What is a class?
''' A class is a template that describes the attributes and behaviors that objects made from it will have.'''

# 2. What is an object?
'''An object is a single instance of a class with its ownpecific data stored in its attributes.'''

# 3. What does self represent?
'''self is a reference to the object calling the method. It lets us read and change that specific object's data'''
