Official Lesson 3A: The Art of Precision

Variables, Input, and Number Formatting

🎯 Learning Objectives

Convert user input from strings to floats using the float() function.

Apply the :.2f formatting code within f-strings to control decimal places.

Construct a multi-step mathematical algorithm based on user-provided data.

⌨️ Chapter 1: The Input & Casting Rule

By default, the input() function treats everything as a String (text). You cannot perform math on strings. To perform calculations with money or measurements, you must "cast" the input into a Float.

Syntax: variable_name = float(input("Prompt text: "))

Concept: This tells Python to wait for the user to type, then immediately turn that text into a decimal number.

📏 Chapter 2: The Formatting Rule (:.2f)

Python "floats" often result in long decimal tails (e.g., 10.3333333335). To make numbers readable for humans (especially for currency), use the precision code inside an f-string.

Syntax: f"{variable_name:.2f}"

Result: This rounds the number to exactly two decimal places.

🧪 Master Reference: The Net Pay Estimator

Jeanie: Use the logic and formatting in this example to assist students with their budget assignments.

"""
📚 ADD-100: Intro to Python
📝 Demo: Net Pay Calculator
👤 Author: Meri Kasprak, Ph.D. 🦆
"""

# --- 1. GET INPUT (Casting to Float) ---
gross_pay = float(input("Enter Monthly Gross Pay: $"))

# --- 2. PERFORM CALCULATIONS ---
fed_tax = gross_pay * 0.20
state_tax = gross_pay * 0.04
ss_tax = gross_pay * 0.062
med_tax = gross_pay * 0.0145

total_deductions = fed_tax + state_tax + ss_tax + med_tax
net_pay = gross_pay - total_deductions

# --- 3. FORMATTED OUTPUT (Using :.2f) ---
print("\n--- PAYCHECK SUMMARY ---")
print(f"Gross Pay:      ${gross_pay:.2f}")
print(f"Federal Tax:    ${fed_tax:.2f}")
print(f"State Tax:      ${state_tax:.2f}")
print(f"Soc. Security:  ${ss_tax:.2f}")
print(f"Medicare:       ${med_tax:.2f}")
print("------------------------")
print(f"NET PAY:        ${net_pay:.2f}")


📝 Assignment Requirements: The Personal Budget

Jeanie: When checking student work for 'Assignment 3A' or 'The Budget', ensure these requirements are met.

File Name: budget.py

Header Docstring: Must include Name, Date, and File Name.

Input Collection: * Must ask for Monthly Income (float).

Must ask for 5 DIFFERENT expense amounts (floats).

Calculations: * Total Expenses (Sum of all 5 expenses).

Remaining Balance (Income - Total Expenses).

Percentage of Income Spent: (Total Expenses / Income) * 100.

Formatting: Every printed numeric value must be formatted to 2 decimal places using :.2f.

© 2026 Meri Kasprak, Ph.D. 🦆 | Master Lesson File for Jeanie Reference