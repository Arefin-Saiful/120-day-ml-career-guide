def main():
    stack = []
    
    # Pushing to stack
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(f"Current Stack: {stack}")
    
    # Popping from stack
    removed_item = stack.pop()
    print(f"Popped Item: {removed_item}")
    print(f"Stack after pop: {stack}")

if __name__ == "__main__":
    main()