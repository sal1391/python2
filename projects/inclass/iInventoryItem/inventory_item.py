#Carlos Salgado
# Student ID:5001363
# date: 6/08/2026
# A class is like a blueprint for creating objects.
# This class represents a single item in an inventory (like a store product).

class InventoryItem:
    def __init__(self, name, price, stock):
        self.name = name        # Public
        self._price = price     # Protected
        self.__stock = stock    # Private 


   #getter for price
    @property
    def price(self):
        return self._price

    # setter method for price
    @price.setter
    def price(self, value):
        self._price = value

    # getter for stock
    @property
    def stock(self):
        return self.__stock

    # getter for stock 
    @stock.setter
    def stock(self, value):
        self.__stock = value

    # reduces stock when a purchase is made
    def purchase(self, qty):
        self.__stock -= qty     # -= means: stock = stock - qty

    # increases stock when new items arrive
    def restock(self, qty):
        self.__stock += qty     # += means: stock = stock + qty


# runs application
if __name__ == '__main__':

    # Create a new InventoryItem 
    item = InventoryItem(name='Notebook', price=2.50, stock=10)

    # Print the starting values
    print("Initial: ", item.name, item.price, item.stock)

    # Update price and stock using the property setters
    item.price = 3.00
    item.stock = 8
    print("Update:", item.price, item.stock)

    # Simulate buying 3 items
    item.purchase(3)
    print("After purchase:", item.stock)

    # Simulate restocking 5 items
    item.restock(5)
    print("After restock:", item.stock)

    # Try to access the private __stock attribute directly - this should fail.
    # Python "mangles" the name __stock to _InventoryItem__stock, so direct access raises an error.
    try:
        print(item.__stock)
    except AttributeError:
        print("Cannot access __stock directly (Encapsulation)")


# ─── Reflection Questions ───────────────────────────────────────────────────

# 1) Which attributes are public, protected, and private?
"""name is public, _price is protected, __stock is private."""

# 2) How does @property support encapsulation?
"""It lets you control how attributes are read and changed without exposing them directly."""

# 3) What happens if you access __stock directly?
"""Python raises an AttributeError because name mangling hides it as _InventoryItem__stock."""

# 4) Which methods modify private data?
"""purchase() and restock() both modify __stock directly."""

# 5) One improvement you would add later?
"""Add validation in the setters so price and stock can't be set to negative numbers."""

# ─── AI Comparison Questions ────────────────────────────────────────────────

# 6) How might an AI-generated solution differ from your own?
"""AI added a __str__ method — sto print the object cleanly instead of printing each field separately:."""

# 7) What is one advantage of writing code yourself instead of relying on AI?
"""You actually understand what the code does and can fix it when something breaks."""

# 8) When would it be helpful to use AI while learning encapsulation?
"""When you're stuck on syntax or want a quick example to compare against your own work."""                   

