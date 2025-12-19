# Day 4 — Lists (Data Structures I)

## 🎯 Goals
* Understand **Mutability** and memory references.
* Master **List Slicing** `[start:stop:step]`.
* Implement **LIFO Stacks** using `.append()` and `.pop()`.
* Write concise code with **List Comprehensions**.

## 🔨 Work Done
* **The Reference Trap:** Proved that assigning `list_b = list_a` does not copy the data, only the memory address.
* **The Slicing Surgeon:** Used negative stepping to reverse specific sections of a list.
* **The Stack Emulator:** Built a "Last-In, First-Out" data structure.
* **The One-Line Architect:** Generated a filtered list of squares in a single line of code.

## 🧠 Key Learnings
* **Mutability:** Modifying a list variable modifies the object in memory, affecting all other variables pointing to it.
* **Shallow Copy:** Slicing (e.g., `data[:]`) creates a new object, protecting the original list.
* **Performance:** `.append()` is O(1) (instant), while `.insert(0)` is O(N) (slow) because it shifts all elements.
* **List Comprehension:** Faster and cleaner than standard loops for creating new lists.