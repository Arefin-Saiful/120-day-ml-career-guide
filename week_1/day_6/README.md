# Day 6 — Functions & Modularity

## 🎯 Goals
* Understand **Scope** (Local vs. Global) and the Stack Frame.
* Master **Default Arguments** for flexible function calls.
* Learn about **Implicit Returns** (`None`).
* Write cleaner logic by returning Boolean expressions directly.

## 🔨 Work Done
* **The Scope Fortress:** Proved that variables inside a function are local and do not modify global variables of the same name.
* **The Pure Return:** Demonstrated that a function that prints but doesn't `return` actually evaluates to `None`.
* **The Default Gateway:** Created a function that uses a default port number if none is provided.
* **The Logic Gate:** Wrote a one-line validator function that returns the result of a comparison directly.

## 🧠 Key Learnings
* **The Stack Scope:** When a function runs, it creates a temporary "Stack Frame". Variables born there die there.
* **LEGB Rule:** Python looks for variables in this order: **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in.
* **Implicit None:** If you forget `return`, Python secretly executes `return None` at the end.
* **Boolean Efficiency:** You don't need `if condition: return True`; you can simply `return condition`.