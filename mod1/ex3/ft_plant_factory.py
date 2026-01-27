

class Plant:
    """ Plant Class """
    def __init__(self, name: str, height: int, age: int):
        """ Initializer """
        self.name = name
        self.start_height = height
        self.start_age = age
        print(
            f"Created: {self.name}"
            f" ({self.start_height}cm, {self.start_age} days)"
        )


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Oak", 200, 365)
    plant3: Plant = Plant("Cactus", 5, 90)
    plant4: Plant = Plant("Sunflower", 80, 45)
    plant5: Plant = Plant("Fern", 15, 120)
    print("\nTotal plant created: 5")
