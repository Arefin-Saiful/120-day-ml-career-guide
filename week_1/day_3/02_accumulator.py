def main():
    n = 5
    total = 0 # The Accumulator
    
    for i in range(1, n + 1):
        total = total + i # Update state
        print(f"Iteration {i}: total becomes {total}")
        
    print(f"Final Sum: {total}")