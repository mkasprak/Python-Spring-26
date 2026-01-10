import datetime  # Import the datetime library to timestamp our reports

"""
ASSIGNMENT 13B: SPRINT 6 - SYSTEM HARDENING
Project: Quacken Coffee POS (V6.0)
Developer: Monty PyDuck
"""

# GLOBAL CONSTANTS: Pantry Rules
MENU_FILE = "menu.txt"
DATA_FILE = "order_history.txt"
HUMAN_REPORT = "human_report.txt"
MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy", "Coconut")
TAX_RATE = 0.05


def get_customer_info():
    """Hardened identity collection using loops."""
    while True:
        name = input("Customer Name: ").title()
        if len(name) >= 2:
            break
        print("❌ Error: Please enter a name with at least 2 characters.")

    location = input("Office Number: ")
    return name, location


def take_order():
    """Bulletproof input loops for drink selection."""
    print("\n--- CURRENT MENU ---")
    try:
        with open(MENU_FILE, "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("⚠️ Warning: Menu file not found. System using defaults.")

    cat = input("\nDrink Category (Coffee/Tea/Cocoa): ")
    size = input("Size (Small/Medium/Large): ")
    print(f"Available Milk: {MILK_OPTIONS}")
    milk = input("Choice of milk: ")

    # Trapping the user until an integer is provided (The Banana Test)
    while True:
        try:
            pumps = int(input("How many pumps? "))
            if pumps < 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Input Error: Please enter a positive whole number for pumps.")

    return {"category": cat, "size": size, "milk": milk, "pumps": pumps}


def calculate_total(order_data):
    """Calculates price with self-healing file logic."""
    base_price = 4.00
    try:
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
    except Exception:
        print("⚠️ System Error: Using default base price ($4.00)")

    syrup_cost = order_data["pumps"] * 0.10
    subtotal = base_price + syrup_cost
    tax_amt = subtotal * TAX_RATE
    return subtotal + tax_amt, tax_amt


def save_data_and_label(customer, location, total, tax):
    """Saves raw data and uses ELSE for confirmation."""
    try:
        with open(DATA_FILE, "a") as f:
            f.write(f"{customer},{location},{total:.2f}\n")
    except Exception as e:
        print(f"❌ Persistence Error: {e}")
    else:
        # Only runs if file append succeeded
        print(f"✅ Order for {customer} saved to {DATA_FILE}")
    finally:
        # Always runs to update the human report
        with open(HUMAN_REPORT, "w") as f:
            f.write(f"BARISTA TICKET - {datetime.date.today()}\n")
            f.write(f"ROOM: {location} | ATTN: {customer}\n")
            f.write(f"TAX: ${tax:.2f} | TOTAL: ${total:.2f}\n")
        print("🏁 Barista report updated.")


def main():
    name, location = get_customer_info()
    current_order = take_order()
    final_price, calculated_tax = calculate_total(current_order)

    save_data_and_label(
        customer=name, location=location, total=final_price, tax=calculated_tax
    )


main()
