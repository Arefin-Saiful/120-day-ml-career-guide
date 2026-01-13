class Wallet:
    def __init__(self, balance):
        self.balance = balance

    # 12.9: Operator Overloading
    # Allows us to use '+' between two Wallet objects
    def __add__(self, other):
        return Wallet(self.balance + other.balance)

    # 12.10: Equality
    # Allows us to compare wallet1 == wallet2 by value, not memory address
    def __eq__(self, other):
        return self.balance == other.balance

    def __str__(self):
        return f"${self.balance}"

# 12.7: Inheritance
# Admin inherits everything from User (reusing code from File 1 logic)
class Admin(Wallet): 
    def __init__(self, balance, level):
        # 12.8: The Super Proxy
        # Calls the parent (Wallet) constructor to handle the balance setup
        super().__init__(balance)
        self.level = level

    def delete_db(self):
        print(f"Admin (Level {self.level}) deleted the database.")

def main():
    w1 = Wallet(100)
    w2 = Wallet(100)
    w3 = Wallet(50)

    print(f"Wallets Equal? {w1 == w2}") # True (thanks to __eq__)
    
    # Polymorphism: Adding objects naturally
    w_total = w1 + w3 
    print(f"Total Wealth: {w_total}") # $150 (thanks to __add__)

    # Admin Logic
    root = Admin(1000, "High")
    root.delete_db()

if __name__ == "__main__":
    main()