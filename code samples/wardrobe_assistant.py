"""
📚 ADD-100: Intro to Python
📝 Demo: Nested Decisions (Wardrobe)
👤 Author: Meri Kasprak, Ph.D. 🦆
"""

# 1. Ask the user for the temp
temp = int(input("What is the temperature (F)? "))

# 2. Main Decision: Is it cold?
if temp <= 32:
    print("It is freezing!")
    # NESTED DECISION (Inside the 'if')
    snow = input("Is it going to snow? (yes/no): ")
    if snow == "yes":
        print("Wear boots and a parka.")
    else:
        print("Wear a heavy coat.")

else:
    print("It is warm enough for rain.")
    # NESTED DECISION (Inside the 'else')
    rain = input("Is it going to rain? (yes/no): ")
    if rain == "yes":
        print("Bring an umbrella.")
    else:
        print("Sneakers are fine.")
