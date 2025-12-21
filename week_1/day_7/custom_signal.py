def main():
    try:
        number = int(input("Enter a positive number: "))
        if number < 0:
            raise ValueError("No negatives allowed!")
        print(f"You entered: {number}")
    except ValueError as e:
        print(f"Custom Rule Violation: {e}")

if __name__ == "__main__":
    main()