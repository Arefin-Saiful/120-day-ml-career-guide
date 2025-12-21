# Day 7 — Error Handling (Exceptions)

## 🎯 Goals
* Master **Defensive Programming** using `try/except`.
* Handle specific crashes like `ValueError` and `ZeroDivisionError`.
* Use `finally` to ensure cleanup (closing files/connections).
* Enforce custom logic using `raise`.

## 🔨 Work Done
* **The Input Guard:** Prevented program crashes when a user types text instead of a number.
* **The Math Safety Net:** Handled mathematical impossibilities (division by zero) without stopping the data pipeline.
* **The Cleanup Crew:** Used a `finally` block to guarantee code execution regardless of errors, simulating resource management.
* **The Custom Signal:** Manually triggered a `ValueError` to enforce specific logic rules (no negative numbers).

## 🧠 Key Learnings
* **Exception Bubbling:** Errors "bubble up" the call stack; if uncaught, they crash the program.
* **Specific Catching:** It is better to catch specific errors (like `ValueError`) than a generic `Exception`.
* **Finally:** This block is critical for preventing memory leaks by closing database connections or file handles, even if the code crashes.
* **Raising:** You can stop execution intentionally using `raise` when data violates business rules.