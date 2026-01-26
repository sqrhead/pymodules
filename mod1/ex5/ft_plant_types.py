
class Plant:
    """ Base Plant class"""

    def __init__(self, name, age, height):
        """ Initializer  """
        self.name: str = name
        self.age: int = age
        self.height: int = height


class Flower(Plant):
    """ Flower class, inherits from Plant"""

    def __init__(self, name, age, height, color):
        """ Initializer  """
        super().__init__(name, age, height)
        self.color: str = color
        print(
            f"{self.name} (Flower): "
            f"{self.height}cm, {self.age} days, {self.color} color"
        )

    def bloom(self) -> None:
        """ bloom function requested from subject """
        print(f"{self.name} is blooming beautifully!\n")
        return


class Tree(Plant):
    """ Tree class, inherits from Plant"""

    def __init__(self, name, age, height, trunk_diameter):
        """ Initializer  """
        super().__init__(name, age, height)
        self.trunk_diameter: int = trunk_diameter
        print(
            f"{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )

    def produce_shade(self) -> None:
        """ produce_shade function requested from subject """
        print(
            f"{self.name} provides "
            f"{self.trunk_diameter * self.height} squares meters of shade\n"
        )
        return


class Vegetable(Plant):
    """ Vegetable class, inherits from Plant"""

    def __init__(self, name, age, height, harvest_season, nutritional_value):
        """ Constructor  """
        super().__init__(name, age, height)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value
        print(
            f"{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )
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
