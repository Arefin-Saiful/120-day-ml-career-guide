def main():
    # Theoretical Demonstration
    print("Why are Hash Maps faster?")
    print("1. List: Python scans item 1, item 2, item 3... until found.")
    print("2. Dict: Python runs hash(key) -> gets address 0x99 -> looks only there.")
    print("Result: Lookup is instant, even with 1 million items.")

if __name__ == "__main__":
    main()