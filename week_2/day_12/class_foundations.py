class User:
    def __init__(self, name, password):
        # 12.1: The Constructor initializes the object's state
        self.name = name
        self.is_active = True
        
        # 12.4: Private Variables (Name Mangling)
        # Python renames this to _User__password to prevent accidental access
        self.__password = password
    
    # 12.2: Self Reference
    # 'self' is required to access the specific instance's data (e.g., this user's name)
    def login(self, password):
        if password == self.__password:
            print(f"Welcome back, {self.name}!")
        else:
            print("Invalid credentials.")

    # 12.3: String Representation
    # For end-users (print(user))
    def __str__(self):
        return f"User: {self.name} (Active: {self.is_active})"

    # For developers (debugging)
    def __repr__(self):
        return f"User(name='{self.name}', active={self.is_active})"

def main():
    u = User("Alice", "secret123")
    print(u)           # Triggers __str__
    u.login("secret123")
    
    # Trying to access private variable (Uncomment to see error)
    # print(u.__password) # AttributeError

if __name__ == "__main__":
    main()