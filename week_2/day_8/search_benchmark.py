# Challenges 8.1, 8.2, 8.6, 8.9
# Goal: Compare List Search vs Set Search vs Length Check
import time

def main():
    N = 10_000_000  # 10 Million items
    print(f"--- Generatng list of {N} items... ---")
    data_list = list(range(N))
    
    # 1. The Linear Scan (O(N))
    print("\n[1] Linear Scan (List)")
    start = time.time()
    found = -5 in data_list  # Worst case: scans entire list
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")
    
    # 2. The Hash Lookup (O(1))
    print("\n[2] Hash Lookup (Set conversion + Search)")
    # Note: Building the set takes O(N), but the search itself is O(1)
    data_set = set(data_list) 
    start = time.time()
    found = -5 in data_set  # Instant lookup via hash address
    end = time.time()
    print(f"Time taken: {end - start:.6f} seconds")

    # 3. The Length Trick (O(1))
    print("\n[3] Length Check (len())")
    start = time.time()
    length = len(data_list) # Reads cached ob_size metadata
    end = time.time()
    print(f"Time taken: {end - start:.10f} seconds (Instant)")

if __name__ == "__main__":
    main()