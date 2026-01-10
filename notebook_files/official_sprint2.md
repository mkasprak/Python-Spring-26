🤖 Architect Jeanie’s Sprint 2: The Functional Blueprint
Role: Scrum Master

Focus: Functional Architecture & Data Handoffs

Project: Quacken Coffee POS (V1.0)

🏗️ From Blueprint to Plumbing
"Lead Developer, it’s time to turn your Word document blueprints into Python reality. In professional engineering, we don't build the whole house at once. We start with Stubs—placeholders that define the 'plumbing' of our data before we turn on the 'water' of our logic."

📋 Concept 1: What belongs in a Function?
In a professional system, main() is the Conductor. It shouldn't do the heavy lifting (like math or file saving); it should simply call the specialized "Processors" to do the work.

Your System's Processors:
The Identity Phase: A function to capture the Customer Name and Office Location.

The Collection Phase: A function to capture the Category (Coffee, Tea, Cocoa), Size, Milk Type (including Soy and Coconut), and Pumps.

The Calculation Phase: A function that takes that data and returns a Total Price.

The Persistence Phase: A function that handles saving the Raw Data Log and printing the Human Label.

🤝 Concept 2: The Data Handoff (Return & Parameters)
The most important skill this week is the Handoff.

When a function finishes its job, it must return the data back to main().

main() then saves that data in a variable and passes it as an argument to the next function.

🛠️ Your Architecture Checklist
To pass this Sprint Review, your code stub must show:

Header Docstring: Every file starts with the project name and your name as Developer.

Function Docstrings: Every def must have a triple-quoted string explaining what it will do.

# TODO Comments: Use these as markers for the logic we haven't learned yet (like reading from menu.txt).

No "Naked" Code: All logic must live inside a function.

⚠️ Jeanie's Warning: The "NoneType" Error
"If you forget to use the return keyword at the end of a function, main() will receive nothing (None). This is like a relay racer dropping the baton. Check your returns before you submit your stub!"