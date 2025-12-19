def main():
    a = [1, 2, 3]
    b = a  # This is the trap! Both names point to the same object.
    
    b[0] = 99
    
    print(f"List b: {b}")
    print(f"List a: {a}") # 'a' is also changed
    print("Explanation: Both variables point to the same memory block.")

    # Fix: Use copy()
    c = a.copy()
    c[0] = 100
    print(f"List c (copy): {c}")
    print(f"List a (original): {a}") # 'a' remains safe

if __name__ == "__main__":
    main()