"""
📚 ADD-100: Intro to Python
📝 Demo: Net Pay Calculator
👤 Author: Meri Kasprak, Ph.D. 🦆
"""

# --- 1. GET INPUT ---
gross_pay = float(input("Enter Monthly Gross Pay: $"))
# float("400") - this would convert the string to a float - 400.0

# --- 2. PERFORM CALCULATIONS ---
fed_tax = gross_pay * 0.20
state_tax = gross_pay * 0.04
ss_tax = gross_pay * 0.062
med_tax = gross_pay * 0.0145

total_deductions = fed_tax + state_tax + ss_tax + med_tax
net_pay = gross_pay - total_deductions

# --- 3. FORMATTED OUTPUT ---
print("\n--- PAYCHECK SUMMARY ---")
print(f"Gross Pay:      ${gross_pay:,.2f}")
# .2f - float with two places to the right of the decimal
print(f"Federal Tax:    ${fed_tax:,.2f}")
print(f"State Tax:      ${state_tax:,.2f}")
print(f"Soc. Security:  ${ss_tax:,.2f}")
print(f"Medicare:       ${med_tax:,.2f}")
print("------------------------")
print(f"NET PAY:        ${net_pay:,.2f}")
