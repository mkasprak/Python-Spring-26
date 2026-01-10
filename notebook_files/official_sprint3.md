🤖 Architect Jeanie’s Sprint 3: The Customization Engine
Role: Scrum Master

Focus: Data Accountability & System Resilience

Project: Quacken Coffee POS (Hardening Phase)

🛑 The "Variable Swap" Crisis
"Lead Developer, as your system grows, your functions are starting to ask for more data. If you pass five variables in a row (e.g., take_order(c, l, d, m, p)), it is far too easy to accidentally swap the 'Milk' with the 'Location.' In a professional system, this leads to a 'Soy Incident.' This week, we implement Keyword Arguments to ensure every piece of data is labeled."

🌍 Concept 1: Global Constants (The Pantry)
Some data belongs to the whole shop, not just one function. We define these at the very top of our script using ALL_CAPS naming.

Why? If the price of a Small coffee changes, you change it in one place (the constant) rather than hunting through six different functions.

Monty's Standard: MILK_OPTIONS = ("Dairy", "Oat", "Almond", "Soy", "Coconut")

🏷️ Concept 2: Keyword Arguments (The Labels)
When calling a function in main(), we are now moving away from "Positional" arguments.

Old Way: generate_ticket(c, l, d, m, p)

Architect Way: generate_ticket(customer=c, location=l, drink=d, milk=m, pumps=p)

By labeling the data as it enters the function, we make the code self-documenting and prevent the logic from breaking if we change the order of parameters later.

🛡️ Concept 3: Default Values & Resilience
What if a customer doesn't want syrup? We don't want the program to crash or force them to type "0" if we can help it.

We set Default Parameters in our function definitions: def take_order(pumps=0):

We use Try/Except blocks to catch users who type "Two" instead of "2."

⚠️ Jeanie's Audit Note: The "Scope" Rule
"Remember: Functions can see Global Constants, but they cannot see variables living inside other functions. If you need data from get_customer_info() to reach save_data(), it must pass through main(). Don't try to take shortcuts with global variables for user data!"