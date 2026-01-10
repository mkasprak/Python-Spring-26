import datetime  # Import the datetime library to timestamp our reports

"""
ASSIGNMENT 12B: SPRINT 5 - DATA PERSISTENCE
Project: Quacken Coffee POS (V5.0)
Developer: Monty PyDuck
"""

# GLOBAL CONSTANTS: Pantry Rules
MENU_FILE = "code samples/menu.txt"
DATA_FILE = "order_history.txt"
HUMAN_REPORT = "human_report.txt"
MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy", "Coconut")
TAX_RATE = 0.05


def get_customer_info():
    """Asks for name and office location."""
    name = input("Customer Name: ").title()
    location = input("Office Number: ")
    return name, location


def take_order():
    """Reads the menu from file and collects choices."""
    print("\n--- CURRENT MENU ---")
    # Using 'with open' as a context manager ensures the file closes automatically
    with open(MENU_FILE, "r") as f:
        for line in f:
            print(line.strip())

    cat = input("\nDrink Category (Coffee/Tea/Cocoa): ")
    size = input("Size (Small/Medium/Large): ")
    print(f"Available Milk: {MILK_OPTIONS}")
    milk = input("Choice of milk: ")
    try:
        pumps = int(input("How many pumps? "))
    except ValueError:
        pumps = 0
    return {"category": cat, "size": size, "milk": milk, "pumps": pumps}


def calculate_total(order_data):
    """Calculates price by reading menu.txt. Returns TWO values."""
    base_price = 4.00
    # Logic to find price in file
    with open(MENU_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == order_data["category"]:
                if order_data["size"] == "Small":
                    base_price = float(parts[1])
                elif order_data["size"] == "Medium":
                    base_price = float(parts[2])
                else:
                    base_price = float(parts[3])

    syrup_cost = order_data["pumps"] * 0.10
    subtotal = base_price + syrup_cost
    tax_amt = subtotal * TAX_RATE
    return subtotal + tax_amt, tax_amt


def save_data_and_label(customer, location, total, tax):
    """Saves raw data to log and overwrites a human receipt file."""
    # 1. Append raw data for computer logs
    with open(DATA_FILE, "a") as f:
        f.write(f"{customer},{location},{total:.2f}\n")

    # 2. Write (Overwrite) human readable report
    with open(HUMAN_REPORT, "w") as f:
        f.write(f"BARISTA TICKET - {datetime.date.today()}\n")
        f.write(f"ROOM: {location} | ATTN: {customer}\n")
        f.write(f"TAX: ${tax:.2f} | TOTAL: ${total:.2f}\n")


def main():
    # 1. Identity Phase
    name, location = get_customer_info()

    # 2. Data Collection Phase
    current_order = take_order()

    # 3. Calculation Phase & UNPACKING
    final_price, calculated_tax = calculate_total(current_order)

    # 4. Persistence Phase
    save_data_and_label(
        customer=name, location=location, total=final_price, tax=calculated_tax
    )
    print(f"\n✅ Files Updated: {DATA_FILE} and {HUMAN_REPORT}")


main()
