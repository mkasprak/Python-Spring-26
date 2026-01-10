"""
============================================================
☕ QUACKEN COFFEE POS SYSTEM
============================================================

This is the MAIN PROGRAM.

This file:
• talks to the user
• creates drink objects
• allows edits (CRUD)
• saves orders
• prints drink labels

This file USES drink_order.py
It does not define drink classes itself.
"""

import datetime
from drink_order import CoffeeOrder, TeaOrder, CocoaOrder

# ---------------- CONSTANTS ----------------
DATA_FILE = "order_history.txt"
LABEL_FILE = "human_report.txt"

SYRUP_FLAVORS = ("Vanilla", "Caramel", "Hazelnut", "Mocha")
TEA_ADD_INS = ("Lemon", "Honey", "Sugar")
MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy")


# =========================================================
# 👤 CUSTOMER INFO
# =========================================================


def get_customer_info():
    """
    Ask for customer name and office number.
    Uses a loop to prevent bad input.
    """
    while True:
        name = input("Customer Name: ").title()
        if len(name) >= 2:
            break
        print("❌ Name must be at least 2 characters.")

    location = input("Office Number: ")
    return name, location


# =========================================================
# 🧠 ORDER CREATION
# =========================================================


def take_order(name, location):
    """
    Create the correct drink object
    based on the user's choice.
    """
    print("\n--- NEW ORDER ---")
    category = input("Drink (Coffee / Tea / Cocoa): ").title()
    size = input("Size (Small / Medium / Large): ").title()

    while True:
        try:
            pumps = int(input("Syrup pumps: "))
            if pumps < 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Enter a positive whole number.")

    if category == "Coffee":
        print("Syrup flavors:", SYRUP_FLAVORS)
        syrup = input("Choose syrup flavor: ").title()
        return CoffeeOrder(name, location, category, size, pumps, syrup)

    elif category == "Tea":
        flavor = input("Tea flavor: ").title()
        print("Add-ins:", TEA_ADD_INS)
        add_in = input("Choose add-in: ").title()
        return TeaOrder(name, location, category, size, pumps, flavor, add_in)

    elif category == "Cocoa":
        print("Milk options:", MILK_OPTIONS)
        milk = input("Milk choice: ").title()
        whipped = input("Whipped cream? (y/n): ").lower() == "y"
        return CocoaOrder(name, location, category, size, pumps, milk, whipped)

    else:
        print("❌ Unknown drink type. Defaulting to Coffee.")
        return CoffeeOrder(name, location, "Coffee", size, pumps, "Vanilla")


# =========================================================
# 🏷️ SAVE + LABEL PRINTING
# =========================================================


def save_final_data(order):
    """
    Save the order and print a drink label.

    • order_history.txt = long-term record
    • human_report.txt  = drink label (printer behavior)
    """

    # Save history
    with open(DATA_FILE, "a") as f:
        f.write(
            f"{order.customer},{order.location},"
            f"{order.category},{order.get_total():.2f}\n"
        )

    # Print label
    with open(LABEL_FILE, "w") as f:
        f.write("☕ QUACKEN COFFEE ☕\n")
        f.write("-" * 25 + "\n")
        f.write(f"Name:   {order.customer}\n")
        f.write(f"Office: {order.location}\n")
        f.write(f"Drink:  {order.category}\n")
        f.write(f"Size:   {order.size}\n")
        f.write(f"Pumps:  {order.pumps}\n")

        if hasattr(order, "syrup_flavor"):
            f.write(f"Syrup:  {order.syrup_flavor}\n")

        f.write(f"Total:  ${order.get_total():.2f}\n")
        f.write(f"Date:   {datetime.date.today()}\n")

    print("✅ Order saved and label printed.")


# =========================================================
# 🚀 MAIN PROGRAM
# =========================================================


def main():
    print("☕ QUACKEN COFFEE POS ☕")

    name, location = get_customer_info()
    order = take_order(name, location)

    # ---------------- CRUD REVIEW LOOP ----------------
    while True:
        order.display_order()
        edit = input("\nEdit anything? (y/n): ").lower()
        if edit != "y":
            break

        line = input("Line number to edit: ")

        if line == "1":
            order.set_customer(input("New name: "))
        elif line == "2":
            order.set_location(input("New office: "))
        elif line == "3":
            order.set_size(input("New size: "))
        elif line == "4":
            try:
                order.set_pumps(int(input("New pump count: ")))
            except ValueError:
                print("❌ Invalid number.")

        elif isinstance(order, CoffeeOrder) and line == "5":
            order.set_syrup_flavor(input("New syrup flavor: "))

        elif isinstance(order, TeaOrder):
            if line == "5":
                order.set_flavor(input("New tea flavor: "))
            elif line == "6":
                order.set_add_in(input("New add-in: "))

        elif isinstance(order, CocoaOrder):
            if line == "5":
                order.set_milk(input("New milk: "))
            elif line == "6":
                order.set_whipped(input("Whipped? (y/n): ").lower() == "y")

        else:
            print("❌ Invalid choice.")

    save_final_data(order)
    print("🏁 Process complete.")


# =========================================================
# 🔐 SYSTEM IGNITION GUARD (VERY IMPORTANT)
# =========================================================
# This ensures the program only runs when THIS file is executed.
# It prevents accidental execution when imported.
# =========================================================

if __name__ == "__main__":
    main()
