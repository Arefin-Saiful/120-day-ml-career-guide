# Day 3 — Loops and Iteration

## 🎯 Goals
* [cite_start]Master the **Iterator Protocol** in Python.
* Automate tasks using `while` and `for` loops.
* [cite_start]Control flow using `break` (exit) and `continue` (skip).
* [cite_start]Understand **State Retention** using the Accumulator Pattern.

## 🔨 Work Done
* [cite_start]**The Infinite Guardian:** Implemented a `while True` loop that runs until a specific user input ("stop") breaks it.
* [cite_start]**The Accumulator:** Manually calculated a sum sequence to understand how variables persist outside the loop scope.
* [cite_start]**The Efficient Skipper:** Used `continue` to filter out specific numbers from a data stream.
* [cite_start]**The String Walker:** Iterated through string characters to verify Python's iterable behavior.

## 🧠 Key Learnings
* [cite_start]**Infinite Loops:** `while True` creates an infinite cycle at the CPU level; it requires a manual `break` condition.
* [cite_start]**State Retention:** Variables defined *inside* a loop reset every time; variables defined *outside* persist (accumulate).
* [cite_start]**Short-Circuiting:** `continue` tells the interpreter to ignore the rest of the block and jump to the next item immediately.
* [cite_start]**Iterator Protocol:** When looping over a string, Python implicitly calls `next()` to fetch characters one by one.

## 🛑 Blockers / Questions
* None