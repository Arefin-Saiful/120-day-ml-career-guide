def main():
    defaults = {"theme": "light", "audio": "on"}
    user_pref = {"theme": "dark"}
    
    # Using the update operator (Python 3.9+)
    # Python calculates hash of "theme", finds it exists, and Overwrites it.
    config = defaults | user_pref
    
    print(f"Merged Config: {config}")

if __name__ == "__main__":
    main()