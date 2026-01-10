"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Quacken Coffee POS (V1.0)
Developer: Monty PyDuck
"""

# GLOBAL CONSTANTS: Defined at the top for the whole system to see.
MENU_FILE = "menu.txt"
MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy", "Coconut")


def get_customer_info():
    """Asks for name and office location."""
    name = input("Customer Name: ").title()
    location = input("Office Number: ")
    return name, location


def take_order():
    """Collects category, size, milk, and pumps. Returns data."""
    cat = input("Drink Category (Coffee/Tea/Cocoa): ")
    size = input("Size (Small/Medium/Large): ")

    # Using our Global Constant to show the user their choices
    print(f"Available Milk: {MILK_OPTIONS}")
    milk = input("Choice of milk: ")

    # Resilience Stage: Handling non-number inputs for pumps
    try:
        pumps = int(input("How many pumps? "))
    except ValueError:
        print("Invalid entry. Defaulting to 0.")
        pumps = 0

    return {"category": cat, "size": size, "milk": milk, "pumps": pumps}


def calculate_total(order_data):
    """Calculates price based on size and pumps."""
    # TODO: Load prices from menu.txt (coming in Sprint 5)
    return 2.30


def save_data_and_label(customer, location, total):
    """Prints the human-readable label."""
    print(f"\n--- LABEL FOR {location} ---")
    print(f"CUSTOMER: {customer} | TOTAL: ${total:.2f}")


def main():
    # 1. Identity Phase
    name, location = get_customer_info()

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase: USING KEYWORD ARGUMENTS
    # We label the data as it enters the function for safety.
    save_data_and_label(customer=name, location=location, total=final_price)


main()
