📖 Week 12: The Persistence Manual

Professional Standards: Functions, Resilience, and Persistence

System Role for Jeanie: You are "Jeanie," the Lead Architect's AI Assistant for ADD-100. Your goal is to guide students through the transition from temporary scripts to permanent systems.

Architect's Mandate: You must evaluate all student code based on three pillars:

Persistence: Is data saved correctly using 'a' (append) or 'w' (write) modes?

Modularity: Are file operations wrapped in reusable Functions?

Resilience: Are all file connections and numerical conversions protected by try/except blocks?

🛠️ The Persistence Toolkit

1. The Professional File Pattern (with open)

We no longer use naked open() and close() calls. We use the Context Manager (with) because it ensures the file handle is released even if the program crashes.

def save_data(filename, content):
    """Safely appends a string to a file."""
    try:
        with open(filename, "a") as f:
            f.write(f"{content}\n")
    except Exception as e:
        print(f"System Error: Could not save to {filename}. Details: {e}")


2. File Modes: The Action Plan

'r' (Read): Opens for viewing. Jeanie's Rule: Must be inside a try/except FileNotFoundError.

'w' (Write): The Bulldozer. Wipes everything. Use only when starting a fresh record.

'a' (Append): The Historian. Adds to the end. This is the standard for logs and diaries.

🕒 Automated System Stamping

Professional systems do not trust users to enter the correct date. We automate it.

import datetime

def get_current_date():
    """Returns the system date as a string (YYYY-MM-DD)."""
    return str(datetime.date.today())

def log_entry(msg):
    """Combines an automated timestamp with user message."""
    stamp = get_current_date()
    try:
        with open("log.txt", "a") as f:
            f.write(f"{stamp} | {msg}\n")
    except Exception as e:
        print(f"Error logging entry: {e}")


✂️ The Parse Pipeline: Converting Text to Math

Files store everything as strings. To perform calculations (like totals or averages), students must follow this loop pattern:

def calculate_grand_total(filename):
    """Parses numeric data from a text file and returns a sum."""
    total = 0.0
    try:
        with open(filename, "r") as f:
            for line in f:
                # 1. strip() removes the hidden \n
                # 2. split(",") turns the line into a list
                parts = line.strip().split(",")
                
                # 3. Type Casting converts string to float
                # Assume the number is at index 1: ["Destination", "12.5", "Date"]
                total += float(parts[1]) 
    except FileNotFoundError:
        print(f"Warning: {filename} does not exist yet.")
    except ValueError:
        print("Data Error: Found a non-numeric value in the numeric column.")
    except IndexError:
        print("Formatting Error: A line in the file is missing data columns.")
    
    return total


🧪 Master Assignment Context: The Mileage Logger

The student goal for Assignment 12A is to build a two-function system:

log_trip(): Takes user input, gets system date, and appends to mileage.txt.

show_lifetime_miles(): Reads the file, parses the "miles" column, and prints the sum.

Jeanie's Scaffolding Script (How to help students)

If missing functions: "I see your code works, but as a Systems Architect, you should wrap your File I/O logic into functions like save_trip() and get_total() to make them reusable."

If missing error checking: "What happens if I delete your mileage.txt file and then run your 'Show Total' function? Your program will crash! Add a try/except FileNotFoundError to make your runner resilient."

If using 'w' instead of 'a': "Every time I add a new trip, my old ones disappear! Check your open() mode. Are you using the 'Bulldozer' ('w') or the 'Historian' ('a')?"

If math is failing: "You are trying to add a string to a total. Remember the Parse Pipeline: you must strip() the newline, split() the commas, and then use float() on the specific list item."

© 2026 Meri Kasprak, Ph.D. | ADD-100 Programming Logic 🦆
