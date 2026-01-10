"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Quacken Coffee POS (Hives-Prevention Version)
Developer: Monty PyDuck
"""

# GLOBAL CONSTANTS (Pantry Rules)
MENU_FILE = "menu.txt"


def get_customer_info():
    """Asks for name and office location."""
    # TODO: Ask for name and office number
    return "Merry McQuacken", "Office 101"


def take_order():
    """Collects category, size, milk, and pumps. Returns data."""
    # TODO: Capture milk (Soy/Coconut/Oat/etc.) and category (Coffee/Tea/Cocoa)
    pass


def calculate_total(order_data):
    """Calculates price based on size and pumps."""
    # TODO: Load prices from menu.txt
    return 2.30


def save_data_and_label(customer, total):
    """Appends to order_history.txt and prints the human-readable label."""
    # TODO: Write raw data for computer and formatted box for barista
    pass


def main():
    # 1. Identity Phase
    name, location = get_customer_info()
    print(f"Customer: {name} | Location: {location}")

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase
    final_price = calculate_total(current_order)

    # 4. Handoff Phase
    save_data_and_label(name, final_price)


main()
