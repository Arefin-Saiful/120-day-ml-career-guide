x = 10 

def change_x():
    x = 20  
    print(f"Inside function: {x}")

def main():
    change_x()
    print(f"Outside function: {x}")

if __name__ == "__main__":
    main()