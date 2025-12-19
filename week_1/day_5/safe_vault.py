def main():
    user = {"id": 1}   
    # Safe Access
    email = user.get("email", "No Email Found")
    print(f"Email: {email}")

if __name__ == "__main__":
    main()