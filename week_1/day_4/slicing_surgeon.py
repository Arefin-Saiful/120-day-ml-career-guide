def main():
    data = [10, 20, 30, 40, 50]
    
    # Syntax: [start:stop:step]
    # -1 is the last item, -4 stops before the 4th item from end, -1 steps backwards
    subset = data[-1:-4:-1] 
    # Alternative: data[:1:-1] (stop at index 1, exclusive)
    
    print(f"Original: {data}")
    print(f"Surgery Result: {subset}")

if __name__ == "__main__":
    main()