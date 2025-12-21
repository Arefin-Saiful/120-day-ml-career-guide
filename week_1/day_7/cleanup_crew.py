def main():
    try:
        num = int(input("Enter a number to divide 100 by: "))
        print(f"Result: {100 / num}")
    except ZeroDivisionError:
        print("Error: Div by Zero.")
    except ValueError:
        print("Error: Invalid number.")
    finally:
        print("Execution Complete (Database/File connections closed).")

if __name__ == "__main__":
    main()