# Challenges 8.5, 8.7, 8.8
import time
import random

def main():
    # 1. The String Builder Trap (O(N^2))
    print("--- String Concatenation vs Join ---")
    iterations = 50_000
    
    # Bad Way (+= creates a new string every time)
    start = time.time()
    s = ""
    for _ in range(iterations):
        s += "a"
    print(f"Loop += :   {time.time() - start:.4f}s")
    
    # Good Way (Join is optimized)
    start = time.time()
    lst = ["a"] * iterations
    s = "".join(lst)
    print(f".join() :   {time.time() - start:.4f}s")

    # 2. Sorting Cost (O(N log N))
    print("\n--- Sorting Random List ---")
    data = [random.randint(0, 100) for _ in range(100_000)]
    start = time.time()
    data.sort() # Uses Timsort
    print(f"Sort 100k items: {time.time() - start:.4f}s")

    # 3. Quadratic Nested Loop (Theory)
    print("\n--- Nested Loop Warning ---")
    print("If we ran a nested loop 10k * 10k, it would be 100M operations.")
    print("We skip running it to save your CPU, but remember: Avoid Nested Loops on large data!")

if __name__ == "__main__":
    main()