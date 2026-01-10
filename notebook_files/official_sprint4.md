🤖 Architect Jeanie’s Sprint 4: The Great Payoff
Role: Scrum Master

Focus: Return Statements, Scope Integrity, and Variable Unpacking

Project: Quacken Coffee POS (Logic Completion)

📦 The "Black Box" Principle
"Lead Developer, a professional function should be a Black Box. Data goes in (parameters), a calculation happens, and a result comes out (return). Up until now, we have been using print() inside our functions. That is a 'Side Effect.' In Sprint 4, we silence the functions so they only speak to the Conductor."

🔄 Concept 1: The Return Statement
When a function uses return, it sends a value back to the line of code that called it.

The Print way: The data is shown on the screen, then disappears. The computer cannot "use" it later.

The Return way: The data is handed back to main(). You can save it, math it, or save it to a file.

🎒 Concept 2: Multiple Returns (The Package)
Sometimes a function does a lot of work and has several results to share. Python allows you to send a "Package" of data.

Example: return final_total, tax_amt

🔓 Concept 3: Unpacking in the Conductor
When main() receives a "Package" (a tuple), it needs to open it. We do this through Unpacking.

The Code: total, tax = calculate_bill(price, pumps)

How it works: Python looks at the two values coming back and assigns the first to total and the second to tax.

⚠️ Jeanie’s Audit: Variable Scope
"I am watching your variables like a hawk this week.

Global Scope: Only for your Constants (ALL_CAPS).

Local Scope: Variables created inside a function (like subtotal) do not exist once the function ends. If you don't return it, you lose it. Don't let your math vanish into the digital void!"

🛠️ Sprint 4 Hardening Checklist
To pass your Mid-Project Audit, ensure:

[ ] No print() statements inside calculate_total().

[ ] main() uses two variables to "catch" the return from your math function.

[ ] Your receipt correctly displays the math results that were handed back.