# Day 8 — The Physics of Code (Time Complexity)

## 🎯 Goals
* Understand **Big O Notation** ($O(1)$, $O(N)$, $O(N^2)$).
* Measure the actual performance difference between Data Structures.
* Learn why `list.insert(0)` and `string +=` are dangerous in large pipelines.

## 🔨 Work Done
* **Search Benchmark:** Proved that Hash Lookups (Sets/Dicts) are instant ($O(1)$) compared to Linear Scans ($O(N)$) which slow down as data grows.
* **List Traps:** Demonstrated that adding/removing items from the *start* of a list forces a massive memory shift ($O(N)$), whereas operations at the *end* are instant ($O(1)$).
* **String Building:** Showed that `"".join()` is significantly faster than using `+=` in a loop because strings are immutable.
* **Slicing & Sorting:** Explored the cost of slicing (allocating new memory) and Python's efficient Timsort algorithm ($O(N \log N)$).

## 🧠 Key Learnings
* **O(1) (Constant):** Instant. `pop()`, `append()`, `len()`, Dictionary Lookup.
* **O(N) (Linear):** Slows down with data size. `pop(0)`, `insert(0)`, `item in list`, String `+=`.
* **O(N^2) (Quadratic):** Nested loops. Avoid these for large datasets!
* **Optimization:** Always prefer `collections.deque` for queues (First-In-First-Out) over standard lists.