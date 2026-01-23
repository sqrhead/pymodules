""" Plant Class """
class Plant:
    """ Constructor """
    def __init__(self, name:str, height:float, age:int):
        self.name = name
        self.height = height
        self.plant_age = age
    """ Utility to log info """
    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")
    """ Requested function for growth """
    def grow(self) -> None:
        self.height = self.height + 1
    """ Requested function for age """
    def age(self) -> None:
        self.plant_age = self.plant_age + 1

if __name__ == "__main__":
    plant: Plant = Plant("Rose", 25, 30)
    old_age: int = plant.plant_age
    print("=== Day 1 ===")
    plant.get_info()
    for i in range(6):
        plant.grow()
        plant.age()
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{plant.plant_age - old_age}cm")
