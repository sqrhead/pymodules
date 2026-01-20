class Plant:
    name: str
    height: float
    start_age: int
    def __init__(self, name:str, height:float, age:int):
        self.name = name
        self.height = height
        self.start_age = age
        print(f"Created: {self.name} ({self.height}cm, {self.start_age} days)")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1: Plant = Plant("Rose", 25, 10)
    plant2: Plant = Plant("Sunflower", 2000, 1)
    plant3: Plant = Plant("Cactus", 120, 50)
    print("Total plant created: 3")

