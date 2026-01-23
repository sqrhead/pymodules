""" Base Plant class"""
class Plant:

    """ Constructor  """
    def __init__(self, name, age, height):
        self.name: str = name
        self.age: int = age
        self.height: int = height

""" Flower class, inherits from Plant"""
class Flower(Plant):

    """ Constructor  """
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color: str = color
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")
    """ bloom function requested from subject """
    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!\n")
        return

""" Tree class, inherits from Plant"""
class Tree(Plant):

    """ Constructor  """
    def __init__(self, name, age, height, trunk_diameter):
        super().__init__(name, age, height)
        self.trunk_diameter: int = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

    """ produce_shade function requested from subject """
    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.trunk_diameter * self.height } squares meters of shade\n")
        return

""" Vegetable class, inherits from Plant"""
class Vegetable(Plant):

    """ Constructor  """
    def __init__(self, name, age, height, harvest_season, nutritional_value):
        super().__init__(name, age, height)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}\n")

if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower1: Flower = Flower("Rose", 20, 30, "Red")
    flower1.bloom()
    flower2: Flower = Flower("Sunflower", 50, 110, "Yellow")
    flower2.bloom()

    tree1: Tree = Tree("Oak", 110, 2100, 100)
    tree1.produce_shade()
    tree2: Tree = Tree("Willow", 30, 100, 40)
    tree2.produce_shade()

    vegetable1: Vegetable = Vegetable("Tomato", 10, 5, "Summer", "C")
    vegetable2: Vegetable = Vegetable("Carrots", 5, 20, "Winter", "B")

