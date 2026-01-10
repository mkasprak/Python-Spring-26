🤖 Architect Jeanie’s Sprint 7: The Object Refactor

Role: Scrum Master

Focus: Class Architecture, Encapsulation, and File Modularity

Project: Quacken Coffee POS (The Modular Engine)

🏗️ From Items to Units

"Lead Developer, we have arrived at the most important architectural shift of the semester. Up until now, you have been a juggler, catching loose variables like name, size, and milk as they fly between functions. This week, we stop juggling and start packing."

💼 Concept 1: The Suitcase (Encapsulation)

In Procedural programming, data is "loose." In Object-Oriented Programming (OOP), we use Encapsulation.

The Suitcase: A Class is a blueprint for a suitcase. It defines what can fit inside.

The Object: An Instance is the actual suitcase you carry. It contains your specific customer, category, and pumps.

The Benefit: Instead of passing five separate variables into a function, you pass one single object. If the object has the data, it also has the power to act on that data!

🗄️ Concept 2: File Modularity (The Blueprint Room)

A professional architect does not leave their blueprints on the construction site floor.

Rule: Your DrinkOrder class must live in its own file named drink_order.py.

Reasoning: This allows multiple different programs to use the same blueprint without re-writing the code. Next week, we will learn how to import this blueprint into your main engine.

🔑 Concept 3: The self Keyword

How does an object know which "name" or "size" belongs to it? It uses the keyword self.

When you write self.customer = customer inside $\_\_init\_\_$, you are telling the object: "Take the name the user gave you and store it in your own internal memory pocket."

Without self, your object has "amnesia" the moment the function ends.

📐 Concept 4: UML Modeling

Before we code, we model. A UML Class Diagram is a three-part box:

The Name: DrinkOrder

Attributes (-): The data the object remembers (private).

Methods (+): The actions the object can perform (public).

🛠️ Sprint 7 Lead Architect Checklist

[ ] Blueprint Separation: Is your DrinkOrder class in a separate .py file?

[ ] Attribute Unit: Does your $\_\_init\_\_$ method capture all five variables (name, category, size, milk, pumps)?

[ ] Self-Awareness: Did you use the self. prefix for every variable the object needs to remember?

[ ] Method Power: Does your class have a get_total() method so the object can calculate its own price?

[ ] Hardened Setters: Did you include a setter method (like set_pumps) to protect your data?