def main():
    while True:
        user_input = input("Type 'stop' to exit: ")
        
        # The Emergency Brake
        if user_input == "stop":
            print("Loop terminated.")
            break
            
        print(f"You typed: {user_input}")