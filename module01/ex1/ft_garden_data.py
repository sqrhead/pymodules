class Plant:
    name: str
    height: float
    age: int
    def __init__(self, name:str, height:float, age:int):
        self.name = name
        self.height = height
        self.age = age
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()