# Day 5 — Dictionaries (Hash Maps)

## 🎯 Goals
* Understand **Hash Tables** and O(1) Lookup speed.
* Handle missing keys safely using `.get()`.
* Perform **Dynamic Key Insertion** for counting/grouping.
* Merge datasets using dictionary updates.

## 🔨 Work Done
* **The Speed Trap:** Analyzed why looking up a key in a Dictionary is instant compared to scanning a List.
* **The Safe Vault:** Used `.get()` to prevent `KeyError` crashes in production code.
* **The Frequency Counter:** Built a manual histogram of character counts.
* **The Database Merger:** Combined two configurations where user preferences override defaults.

## 🧠 Key Learnings
* **O(1) vs O(N):** Lists scan sequentially; Dictionaries jump directly to the memory address via a Hash Function.
* **Safety:** Direct access (`data["key"]`) is risky; `.get()` is the production standard.
* **Hashing:** Keys must be immutable (strings, numbers, tuples) because they need a permanent hash value.