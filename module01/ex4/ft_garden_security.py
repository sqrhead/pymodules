class SecurePlant:
    name: str
    age: int
    height: float

    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height
        print(f"Plant created: {self.name}")
    def get_height(self) -> float:
        return self.height
    def get_age(self) -> int:
        return self.age
    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.height = new_height
        print(f"Heigh updated: {self.height} [OK]")
    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.age = new_age
        print(f"Age updated: {self.age} [OK]")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("Rose",20, 20)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-2)

    print(f"Current plant: {plant.name} ({plant.get_height()}cm, {plant.get_age()} days)")