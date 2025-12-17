def main():
    for i in range(1, 11):
        if i == 5:
            print("(Skipping 5...)")
            continue # Jump back to top of loop immediately
        print(f"Number: {i}")