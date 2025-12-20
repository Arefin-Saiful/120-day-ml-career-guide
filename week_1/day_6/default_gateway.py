def connect(port=3306):
    print(f"Connecting to port {port}...")

def main():
    print("--- Call 1: No Argument ---")
    connect()
    
    print("\n--- Call 2: With Argument ---")
    connect(5432)

if __name__ == "__main__":
    main()