🤖 Architect Jeanie’s Sprint 8: The Inheritance Engine

Role: Scrum Master

Focus: Inheritance, Method Overriding, and Full CRUD Integration

Project: Quacken Coffee POS (The Specialized Build)

🧬 From Objects to Families

"Lead Developer, we have arrived at the final architectural evolution. In Sprint 7, we packed our variables into a suitcase (Class). In Sprint 8, we realize that not all suitcases are the same. A 'Tea' suitcase needs pockets for honey and lemon, while a 'Cocoa' suitcase needs pockets for whipped cream. We don't build three separate classes from scratch; we build a Family Tree."

🌳 Concept 1: Inheritance (The DRY Principle)

DRY = Don't Repeat Yourself.
Instead of writing self.customer = customer in three different files, we write it once in the Parent Class (DrinkOrder).

The Parent: Handles the shared DNA (Name, Location, Size).

The Child: Inherits the DNA and adds its own mutations (Flavor, Whipped Cream).

The Key: super().__init__(...) is the phone call the Child makes to the Parent to say, "Hey, handle the boring stuff so I can focus on the whipped cream."

🎭 Concept 2: Method Overriding (Polymorphism)

Your main engine shouldn't need to know exactly what kind of drink it's holding to display it. It just asks the object, "Show yourself."

The Trick: Every child class has a method named display_order().

The Magic: When main() calls order.display_order(), Python automatically picks the correct version (Coffee, Tea, or Cocoa) to run. This is called Polymorphism.

🕵️ Concept 3: The CRUD Loop & isinstance()

We are building a "Review and Edit" loop. But you can't set "Whipped Cream" on a Coffee object—it would crash.

The Guard: We use if isinstance(order, CocoaOrder): to check the object's type before we try to access specialized data.

The Result: A safe, crash-proof update loop where users can fix typos on line 5 without breaking the system.

🧪 The Gold Master Code (Reference Implementation)

📂 File 1: drink_order.py (The Blueprints)

Save this file in the same folder as your engine. Do not run this file directly.

# drink_order.py: 📦 DRINK CLASS DEFINITIONS

class DrinkOrder:
    def __init__(self, customer, location, category, size, pumps):
        self.customer = customer
        self.location = location
        self.category = category
        self.size = size
        self.pumps = pumps

    def set_customer(self, val): self.customer = val.title()
    def set_location(self, val): self.location = val
    def set_size(self, val): self.size = val.title()
    def set_pumps(self, val):
        if val >= 0: self.pumps = val

    def get_total(self):
        return 4.00 + (self.pumps * 0.10)

class CoffeeOrder(DrinkOrder):
    def __init__(self, customer, location, category, size, pumps, syrup_flavor):
        super().__init__(customer, location, category, size, pumps)
        self.syrup_flavor = syrup_flavor

    def set_syrup_flavor(self, val): self.syrup_flavor = val.title()

    def display_order(self):
        print(f"\n--- ☕ COFFEE ORDER ---")
        print(f"[1] Customer: {self.customer}")
        print(f"[2] Office:   {self.location}")
        print(f"[3] Size:     {self.size}")
        print(f"[4] Pumps:    {self.pumps}")
        print(f"[5] Syrup:    {self.syrup_flavor}")
        print(f"💵 Total: ${self.get_total():.2f}")

class TeaOrder(DrinkOrder):
    def __init__(self, customer, location, category, size, pumps, flavor, add_in):
        super().__init__(customer, location, category, size, pumps)
        self.flavor = flavor
        self.add_in = add_in

    def set_flavor(self, val): self.flavor = val.title()
    def set_add_in(self, val): self.add_in = val.title()

    def display_order(self):
        print(f"\n--- 🍵 TEA ORDER ---")
        print(f"[1] Customer: {self.customer}")
        print(f"[2] Office:   {self.location}")
        print(f"[3] Size:     {self.size}")
        print(f"[4] Pumps:    {self.pumps}")
        print(f"[5] Flavor:   {self.flavor}")
        print(f"[6] Add-in:   {self.add_in}")
        print(f"💵 Total: ${self.get_total():.2f}")

class CocoaOrder(DrinkOrder):
    def __init__(self, customer, location, category, size, pumps, milk, whipped):
        super().__init__(customer, location, category, size, pumps)
        self.milk = milk
        self.whipped = whipped

    def set_milk(self, val): self.milk = val.title()
    def set_whipped(self, val): self.whipped = val

    def display_order(self):
        print(f"\n--- 🍫 COCOA ORDER ---")
        print(f"[1] Customer: {self.customer}")
        print(f"[2] Office:   {self.location}")
        print(f"[3] Size:     {self.size}")
        print(f"[4] Pumps:    {self.pumps}")
        print(f"[5] Milk:     {self.milk}")
        print(f"[6] Whipped:  {'Yes' if self.whipped else 'No'}")
        print(f"Total: ${self.get_total():.2f}")


📂 File 2: quacken_pos.py (The Engine)

Run this file to start the system.

import datetime
from drink_order import CoffeeOrder, TeaOrder, CocoaOrder

# GLOBAL CONSTANTS: Pantry Rules
DATA_FILE = "order_history.txt"
HUMAN_REPORT = "human_report.txt"
MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy", "Coconut")
TEA_ADD_INS = ("Lemon", "Cream", "Honey", "Sugar")
SYRUP_FLAVORS = ("Vanilla", "Caramel", "Hazelnut")

def get_customer_info():
    while True:
        name = input("Customer Name: ").title()
        if len(name) >= 2: break
        print("❌ Name must be at least 2 characters.")
    location = input("Office Number: ")
    return name, location

def take_order(name, location):
    print("\n--- NEW ORDER ---")
    cat = input("Category (Coffee/Tea/Cocoa): ").title()
    size = input("Size: ").title()
    
    while True:
        try:
            pumps = int(input("Syrup Pumps: "))
            if pumps >= 0: break
        except ValueError: print("❌ Invalid number.")

    if cat == "Tea":
        flavor = input("Tea Flavor: ").title()
        add_in = input(f"Add-in {TEA_ADD_INS}: ").title()
        return TeaOrder(name, location, cat, size, pumps, flavor, add_in)
    elif cat == "Cocoa":
        milk = input(f"Milk {MILK_OPTIONS}: ").title()
        whipped = input("Whipped Cream? (y/n): ").lower() == 'y'
        return CocoaOrder(name, location, cat, size, pumps, milk, whipped)
    else:
        # Default to Coffee
        syrup = input(f"Syrup Flavor {SYRUP_FLAVORS}: ").title()
        return CoffeeOrder(name, location, "Coffee", size, pumps, syrup)

def save_final_data(order):
    try:
        with open(DATA_FILE, "a") as f:
            f.write(f"{order.customer},{order.category},{order.get_total():.2f}\n")
        with open(HUMAN_REPORT, "w") as f:
            f.write(f"BARISTA TICKET - {datetime.date.today()}\n")
            f.write(f"ATTN: {order.customer}\n")
            f.write(f"TOTAL: ${order.get_total():.2f}\n")
        print(f"✅ Saved to {DATA_FILE}")
    except Exception as e: print(f"❌ Error: {e}")

def main():
    print("--- QUACKEN POS V8.0 ---")
    name, location = get_customer_info()
    current_order = take_order(name, location)

    while True:
        current_order.display_order()
        if input("\nEdit order? (y/n): ").lower() != 'y': break
        
        line = input("Enter line number: ")
        if line == "1": current_order.set_customer(input("Name: "))
        elif line == "2": current_order.set_location(input("Office: "))
        elif line == "3": current_order.set_size(input("Size: "))
        elif line == "4": 
             try:
                 current_order.set_pumps(int(input("Pumps: ")))
             except ValueError: print("❌ Invalid number")
        
        elif isinstance(current_order, CoffeeOrder) and line == "5":
            current_order.set_syrup_flavor(input("Syrup: "))
        elif isinstance(current_order, TeaOrder):
            if line == "5": current_order.set_flavor(input("Flavor: "))
            elif line == "6": current_order.set_add_in(input("Add-in: "))
        elif isinstance(current_order, CocoaOrder):
            if line == "5": current_order.set_milk(input("Milk: "))
            elif line == "6": current_order.set_whipped(input("Whipped? (y/n): ").lower() == 'y')

    save_final_data(current_order)

if __name__ == "__main__":
    main()


🛠️ Sprint 8 Lead Architect Checklist

[ ] Blueprint Separation: Do you have drink_order.py and quacken_pos.py?

[ ] The Family Tree: Do your child classes use super().__init__?

[ ] Type Safety: Does your update loop use isinstance() to check if the drink is Tea before asking for a flavor?

[ ] The Ignition Guard: Does your main engine end with if __name__ == "__main__":?

© 2026 Meri Kasprak, Ph.D. 🦆

Authorized for Student Use in ADD-100 In Collaboration with Gemini ✨