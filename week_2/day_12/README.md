# Day 12 — The Blueprint (Object-Oriented Programming)

## 🎯 Goals
* Master **Classes & Objects** to bundle data with behavior.
* Implement **Encapsulation** using Private Variables and `@property`.
* Use **Inheritance** to reuse logic and `super()` to extend it.
* Unlock Python's "Magic" with **Operator Overloading** (`__add__`, `__eq__`).

## 🔨 Work Done
* **Class Foundations:** Built a `User` class with a constructor, string representation, and password protection.
* **Encapsulation:** Used the `@property` decorator to calculate age dynamically without storing it, and demonstrated Class vs. Instance variables.
* **Inheritance & Magic:** Created an `Admin` class that inherits from a parent but adds special powers, and enabled math operations on custom objects.

## 🧠 Key Learnings
* **Self:** It is the link between the generic blueprint (Class) and the specific house (Object).
* **Dunder Methods:** `__init__`, `__str__`, and `__add__` allow your objects to behave like native Python types.
* **MRO (Method Resolution Order):** Python looks for methods in the child class first, then the parent, then the grandparent.
* **Polymorphism:** The ability to treat different objects (like `Wallet` and `int`) uniformly using standard operators like `+` or `==`.