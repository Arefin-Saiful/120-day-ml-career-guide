def main():
    x = 0
    try:
        result = 100 / x
        print(result)
    except ZeroDivisionError:
        print("Critical Error: Cannot divide by zero. Skipping operation.")

if __name__ == "__main__":
    main()