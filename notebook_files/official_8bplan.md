🤖 Architect Jeanie’s Sprint 1 Blueprint: The "Hives-Free" System
"Welcome, Lead Developer. We are moving past the 'homework script' phase. Today, we are architecting a persistent system for Quacken Coffee. My role as your Scrum Master is to ensure your logic is sound before you type a single line of code."

📐 The Architect’s Rule: Backwards Design
We do not start with code; we start with the Output. If you know exactly what the cup label needs to look like, you will know exactly what variables your system must collect.

The "North Star" Label Output:
Plaintext

_________________________________
|   QUACKEN COFFEE - OFFICE 101  |  <-- Location
|   CUSTOMER: MERRY MCQUACKEN    |  <-- Identity
|--------------------------------|
|   DRINK: LARGE DECAF COCOA     |  <-- Category/Size
|   MILK:  OAT (ALLERGY SAFE)    |  <-- The "Hives" Driver
|   ADDS:  3 PUMPS VANILLA       |  <-- Calculation Point
|________________________________|
📦 Mandatory System Schema
To meet the Technical Floor for this project, your plan must account for these specific data streams:

Identity & Location: You must track the Customer Name and their Office Number/Location to ensure delivery.

The Milk Prompt: You are required to support: Dairy, Oat, Almond, Soy, and Coconut.

The Pricing Logic:

Small: $1.00

Medium: $1.50

Large: $2.00

Syrup: $0.10 per pump

Persistence Goals: We will eventually save these orders to an order_history.txt file. This allows us to read the data back later to ask: "Would you like your usual order?"

⚠️ Jeanie’s Lead Developer Warning: Scope Creep
"Monty is already talking about drone delivery and mobile apps. That is Scope Creep. We are building an MVP (Minimum Viable Product). Focus on the plumbing: Input, Calculation, and the Safety of the Milk Choice. The drones can wait for Version 2.0."