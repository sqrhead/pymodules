class Plant:
    name: str
    age: int
    height: int
    def __init__(self, name, age, height)
        self.name = name
        self.age = age
        self.height = height

class Flower(Plant):
    color: str
    
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color

    def bloom():
        print(f"{self.name} is blooming beautifully!")
        return

class Tree(Plant):
    trunk_diameter: int
    
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter = trunk_diameter

    def produce_shade():
        print(f"{self.name} provides 78 squares meters of shade")
        return

class Vegetable(Plant):
    harvest_season: str
    nutritional_value: int

    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

if __name__ == "__main__":
    print("=== Garden Plant Types ===")