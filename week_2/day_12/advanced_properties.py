class BiologicalEntity:
    # 12.6: Class Variable
    # Shared by ALL instances. If you change this, it reflects everywhere (unless overridden).
    species = "Human"

    def __init__(self, name, birth_year):
        self.name = name          # Instance Variable (Unique to object)
        self._birth_year = birth_year

    # 12.5: The Property Decorator
    # Looks like a variable access (obj.age), but runs a method.
    # Essential for calculated attributes or encapsulation.
    @property
    def age(self):
        current_year = 2026
        return current_year - self._birth_year

def main():
    p1 = BiologicalEntity("Bob", 1990)
    p2 = BiologicalEntity("Charlie", 2000)

    print(f"{p1.name} is a {p1.species}, Age: {p1.age}")
    
    # Modify Class Variable
    BiologicalEntity.species = "Homo Sapiens"
    print(f"{p2.name} is now a {p2.species}") # Changed for p2 as well!

if __name__ == "__main__":
    main()