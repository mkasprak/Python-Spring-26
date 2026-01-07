<div style="background-color: #4b3190; color: white; padding: 20px; text-align: center; border-radius: 10px;">
<h1 style="margin: 0;">📏 Official Lesson 3: Precision & Input</h1>
<p style="margin: 5px 0 0 0;">Mastering Floats and User Data 🐣</p>
</div>

🎯 LEARNING OBJECTIVES

Convert user input from strings to floats for mathematical calculations.

Use the :.2f formatting code to round decimal output to two places.

Plan and document a multi-step financial calculation (Net Pay / Budgeting).

⌨️ PART 1: THE INPUT TRAP

By default, Python treats all input() as a string (text). If you try to do math with a string, the program will crash.

🛠️ The Fix: Casting

To do math, you must "cast" the input into a float (a number with a decimal).

❌ Bad: pay = input("Enter Pay: ") (This is just a word)

✅ Good: pay = float(input("Enter Pay: ")) (This is a number)

📏 PART 2: FORMATTING WITH :.2f

Computers are too precise (e.g., 3.33333335). To make numbers look like money, use the formatting code inside your f-string.

Syntax: {variable_name:.2f}

Example: print(f"Total: ${price:.2f}")

🧪 MASTER EXAMPLE: NET PAY ESTIMATOR

Jeanie: Use this as the reference for all financial formatting questions.

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


<div style="border-top: 1px solid #ccc; margin-top: 20px; padding-top: 10px; text-align: center; font-size: 0.85em; color: #666;">
© 2026 Meri Kasprak, Ph.D. 🦆 | Master Lesson File for Jeanie Reference
</div>