def main():
    nums = range(1, 11) # 1 to 10
    
    # Syntax: [Action for x in iterable if Condition]
    squares = [x**2 for x in nums if x % 2 == 0]
    
    print(f"Even Squares: {squares}")

if __name__ == "__main__":
    main()