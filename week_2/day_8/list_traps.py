# Challenges 8.3, 8.4, 8.10
# Goal: Demonstrate why insert(0) and pop(0) are slow.
import time
from collections import deque

def main():
    N = 200_000 # Smaller N because O(N) insertion is VERY slow
    data = list(range(N))
    
    # 1. The Insertion Trap
    print(f"--- Comparing Append vs Insert (N={N}) ---")
    
    # Append (O(1))
    start = time.time()
    data.append(999)
    print(f"Append (End): {time.time() - start:.6f}s")
    
    # Insert at Start (O(N) - Forces Shift)
    start = time.time()
    data.insert(0, 999) # Shifts 200k items one step right
    print(f"Insert (Start): {time.time() - start:.6f}s (Much Slower!)")

    # 2. The Queue Bottleneck
    print(f"\n--- Comparing Pop() vs Pop(0) ---")
    
    # Pop from End (O(1))
    start = time.time()
    data.pop()
    print(f"Pop (End):      {time.time() - start:.6f}s")
    
    # Pop from Start (O(N) - Forces Left Shift)
    start = time.time()
    data.pop(0)
    print(f"Pop (Start):    {time.time() - start:.6f}s")
    
    # 3. The Slice Copy
    print(f"\n--- Slice Copy Cost ---")
    # Slicing is O(k) - it allocates NEW memory
    start = time.time()
    new_copy = data[0:100000]
    print(f"Slicing 100k items: {time.time() - start:.6f}s")

if __name__ == "__main__":
    main()