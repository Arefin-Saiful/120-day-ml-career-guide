# Day 2: Logic & Control Flow
# Micro-Challenges from Handbook

def main():
    print("--- Task 1: The Guard Clause ---")
    user = None
    # Short-circuiting prevents crash if user is None
    if user is not None and user == "admin":
        print("User has admin access")
    else:
        print("No access")

    print("\n--- Task 2: Floating Point Trap ---")
    # demonstrating precision issues with binary floating point
    precision_check = 0.1 + 0.2 == 0.3
    print(f"without rounding check is {precision_check}")

    float_sum = 0.1 + 0.2
    rounded_float_check = round(float_sum, 2) == round(0.3, 2)
    print(f"after rounding check is {rounded_float_check}")

    print("\n--- Task 3: Truthiness Inspector ---")
    data = []
    # Implicit boolean check (pythonic way)
    if not data:
        print("empty")
    else:
        print(data)

    print("\n--- Task 4: Ternary Packer ---")
    score = 85
    # One-line conditional assignment
    status = "pass" if score > 70 else "fail"
    print(status)

if __name__ == "__main__":
    main()