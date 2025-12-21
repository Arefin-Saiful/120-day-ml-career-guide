def main():
    try:
        age = int(input("Enter your age: "))
        print(f"Age accepted: {age}")
    except ValueError:
        print("Error: Numbers only, please.")

if __name__ == "__main__":
    main()