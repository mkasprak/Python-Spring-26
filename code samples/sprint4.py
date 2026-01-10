"""
ASSIGNMENT 11B: SPRINT 4 - RETURNS & UNPACKING
Project: Quacken Coffee POS (V1.0)
Developer: Monty PyDuck
"""

# GLOBAL CONSTANTS: Pantry Rules
MENU_FILE = "menu.txt"
MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy", "Coconut")
TAX_RATE = 0.05


def get_customer_info():
    """Asks for name and office location."""
    name = input("Customer Name: ").title()
    location = input("Office Number: ")
    return name, location


def take_order():
    """Collects category, size, milk, and pumps. Returns data."""
    cat = input("Drink Category (Coffee/Tea/Cocoa): ")
    size = input("Size (Small/Medium/Large): ")
    print(f"Available Milk: {MILK_OPTIONS}")
    milk = input("Choice of milk: ")
    try:
        pumps = int(input("How many pumps? "))
    except ValueError:
        pumps = 0
    return {"category": cat, "size": size, "milk": milk, "pumps": pumps}


def calculate_total(order_data):
    """Calculates price based on size and pumps. Returns TWO values."""
    # Temporary pricing logic until Sprint 5
    base_price = 2.00
    syrup_cost = order_data["pumps"] * 0.10
    subtotal = base_price + syrup_cost
    tax_amt = subtotal * TAX_RATE
    final_total = subtotal + tax_amt
    return final_total, tax_amt  # The Return Package


def save_data_and_label(customer, location, total, tax):
    """Prints the human-readable label."""
    print(f"\n--- LABEL FOR {location} ---")
    print(f"CUSTOMER: {customer}")
    print(f"TAX: ${tax:.2f} | TOTAL: ${total:.2f}")


def main():
    # 1. Identity Phase
    name, location = get_customer_info()

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase & UNPACKING
    # We 'catch' the two returned values into two separate variables
    final_price, calculated_tax = calculate_total(current_order)

    # 4. Handoff Phase
    save_data_and_label(
        customer=name, location=location, total=final_price, tax=calculated_tax
    )


main()
