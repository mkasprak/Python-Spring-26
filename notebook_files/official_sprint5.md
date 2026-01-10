🤖 Architect Jeanie’s Sprint 5: Data Persistence
Role: Scrum Master

Focus: File I/O, Data Separation, and Scope Creep

Project: Quacken Coffee POS (The Permanent Record)

💾 The "Architect's Vault"
"Lead Developer, we are moving into the final stage of professional systems: Persistence. Until now, every order you took vanished the moment the program ended. This week, we learn to write to the hard drive so Monty can keep a record of every drop of caffeine sold!"

📂 Concept 1: The Two-File Pattern
In a professional system, we never mix Raw Data with Human Reports.

The Log (order_history.txt): This is for the computer. It is structured (usually comma-separated) so we can read it back into a Python List later.

The Report (human_report.txt): This is for the Barista. It is formatted with lines, headers, and pretty spacing.

📋 Concept 2: The "Review and Edit" Logic
The customer is always right—until they change their mind. To prevent Scope Creep, we aren't building a full database yet, but we are implementing a Review List.

We use with open(FILE, "r") to read the log.

We use .strip().split(",") to turn each text line back into a Python List.

We display the list with enumerate() so the user can pick an ID number to fix a mistake.

🦆 Concept 3: Defeating Scope Creep
Monty wants drones and mobile apps. Your job as the Architect is to say "Not in this Sprint."

MVP (Minimum Viable Product): Does it take the order? Does it save the file? Does it print a receipt? If yes, the Sprint is a success.

The Backlog: Put the "Drone Delivery" ideas in a separate document for Version 2.0.

🛡️ Concept 4: The try/except Shield
File operations are dangerous. What if the file is open in another program? What if it's missing?

Every open() command must live inside a try/except block.

Jeanie will fail your audit if your program crashes just because menu.txt is missing!

🛠️ Sprint 5 Hardening Checklist
[ ] Did you create the menu.txt resource file?

[ ] Does your code read the menu from the file instead of having hard-coded prices?

[ ] Are you appending ("a") to the log but overwriting ("w") the report?

[ ] Can you show a list of previous orders on the screen?