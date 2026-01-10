"""
============================================================
drink_order.py
📦 DRINK CLASS DEFINITIONS (THE MODEL LAYER)
============================================================

This file defines the *types of drinks* the coffee shop can make.

IMPORTANT FOR STUDENTS:
❗ This file does NOT ask the user for input.
❗ This file does NOT run the program.
❗ This file only defines CLASSES (blueprints).

Think of this file like a menu + recipe book.
The POS system will USE these classes, not run them.
"""


class DrinkOrder:
    """
    🧃 BASE CLASS (PARENT CLASS)

    This class represents everything that ALL drinks have in common.

    Every drink has:
    • a customer name
    • an office/location
    • a category (Coffee, Tea, Cocoa)
    • a size
    • syrup pumps
    """

    def __init__(self, customer, location, category, size, pumps):
        # Store basic shared information
        self.customer = customer
        self.location = location
        self.category = category
        self.size = size
        self.pumps = pumps

    # ---------------- CRUD: UPDATE METHODS ----------------
    # These methods allow the POS system to fix mistakes.

    def set_customer(self, val):
        self.customer = val.title()

    def set_location(self, val):
        self.location = val

    def set_size(self, val):
        self.size = val.title()

    def set_pumps(self, val):
        if val >= 0:
            self.pumps = val

    # ---------------- SHARED BUSINESS LOGIC ----------------
    def get_total(self):
        """
        💰 Calculate the price of a drink

        Base price: $4.00
        Each syrup pump: +$0.10
        """
        return 4.00 + (self.pumps * 0.10)


# =========================================================
# ☕ COFFEE ORDER
# =========================================================


class CoffeeOrder(DrinkOrder):
    """
    Coffee is a DrinkOrder with ONE extra feature:
    • syrup flavor
    """

    def __init__(self, customer, location, category, size, pumps, syrup_flavor):
        # Call the parent constructor first
        super().__init__(customer, location, category, size, pumps)
        self.syrup_flavor = syrup_flavor

    def set_syrup_flavor(self, val):
        self.syrup_flavor = val.title()

    def display_order(self):
        """
        📺 Display the order in a readable format.
        Each drink controls how IT is shown.
        """
        print("\n--- ☕ COFFEE ORDER ---")
        print(f"[1] Customer: {self.customer}")
        print(f"[2] Office:   {self.location}")
        print(f"[3] Size:     {self.size}")
        print(f"[4] Pumps:    {self.pumps}")
        print(f"[5] Syrup:    {self.syrup_flavor}")
        print(f"💵 Total: ${self.get_total():.2f}")


# =========================================================
# 🍵 TEA ORDER
# =========================================================


class TeaOrder(DrinkOrder):
    """
    Tea adds:
    • tea flavor
    • add-in (lemon, honey, sugar)
    """

    def __init__(self, customer, location, category, size, pumps, flavor, add_in):
        super().__init__(customer, location, category, size, pumps)
        self.flavor = flavor
        self.add_in = add_in

    def set_flavor(self, val):
        self.flavor = val.title()

    def set_add_in(self, val):
        self.add_in = val.title()

    def display_order(self):
        print("\n--- 🍵 TEA ORDER ---")
        print(f"[1] Customer: {self.customer}")
        print(f"[2] Office:   {self.location}")
        print(f"[3] Size:     {self.size}")
        print(f"[4] Pumps:    {self.pumps}")
        print(f"[5] Flavor:   {self.flavor}")
        print(f"[6] Add-in:   {self.add_in}")
        print(f"💵 Total: ${self.get_total():.2f}")


# =========================================================
# 🍫 COCOA ORDER
# =========================================================


class CocoaOrder(DrinkOrder):
    """
    Cocoa adds:
    • milk type
    • whipped cream choice
    """

    def __init__(self, customer, location, category, size, pumps, milk, whipped):
        super().__init__(customer, location, category, size, pumps)
        self.milk = milk
        self.whipped = whipped

    def set_milk(self, val):
        self.milk = val.title()

    def set_whipped(self, val):
        self.whipped = val

    def display_order(self):
        print("\n--- 🍫 COCOA ORDER ---")
        print(f"[1] Customer: {self.customer}")
        print(f"[2] Office:   {self.location}")
        print(f"[3] Size:     {self.size}")
        print(f"[4] Pumps:    {self.pumps}")
        print(f"[5] Milk:     {self.milk}")
        print(f"[6] Whipped:  {'Yes' if self.whipped else 'No'}")
        print(f"💵 Total: ${self.get_total():.2f}")
