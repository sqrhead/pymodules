""" Plant Class  """
class Plant:
    """ Constructor """
    def __init__(self, name:str, height:float, age:int):
        self.name: str = name
        self.height: float = height
        self.age: int = age
    """ Utility to log infos """
    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()