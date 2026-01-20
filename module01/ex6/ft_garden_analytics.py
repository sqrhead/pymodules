""" Basic Plant class"""
class Plant:
    name: str
    height: int
    age: int
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    """ Grow function to make grow the plants"""
    def grow(self) -> None:
        self.height = self.height + 1
        print(f"{self.name} grew 1cm")

    def log(self) -> None:
        print(f"- {self.name}: {self.height}")

""" FloweringPlant class  """
class FloweringPlant(Plant):
    color: str
    staus: str
    def __init__(self, name, age, height, color, status):
        super().__init__(name, age, height)
        self.color = color
        self.status = status

    def log(self) -> None:
        print(f"- {self.name}: {self.height}, {self.color} flowers ({self.status})")

""" PrizeFlower class  """
class PrizeFlower(FloweringPlant):
    prize_points: int
    def __init__(self, name, age, height, color, status, prize_points):
        super().__init__(name, age, height, color, status)
        self.prize_points = prize_points

    def log(self) -> None:
        print(f"- {self.name}: {self.height}, {self.color} flowers ({self.status}), Prize points: {self.prize_points}")

""" GardenManager class used to manage a gardens duh"""
class GardenManager:

    def __init__(self):
        print("=== Garden Management System Demo ===\n")
        self.gardens: dict[str, list[Plant]] = {} # initialization needed to not get an error
        self.gardens_number: int = 0

    """ GardenStats nested class used as a helper, to display infos"""
    class GardenStats:
        def print_all_owner(gardens: dict[str, list[Plant]]):
            for key in gardens:
                print(f"Garden of {key}")
            print("\n")

        def get_height_validation(gardens: dict[str, list[Plant]]) ->bool:
            for key in gardens:
                for value in gardens[key]:
                    if GardenManager.is_height_valid(value.height) == False:
                        return False

        def print_report(owner: str, gardens: dict[str, list[Plant]]) -> None:
            print(f"\n=== {owner}'s Garden Report ===")
            print("Plants in garden:")
            for value in gardens[owner]:
                value.log()
        def print_general_report(gardens: dict[str, list[Plant]]) -> None:
            return

        def print_stats(gardens: dict[str, list[Plant]]):
            return

    """ Function to add a garden, it just creates a empty list in the dict"""
    def add_garden(self, owner: str) -> None:
        for key in self.gardens:
            if key == owner:
                print("Error: This name is already used")
                return
        self.gardens[owner] = []
        self.gardens_number = self.gardens_number + 1

    """ Function to add a plant to a garden """
    """ Im not checking on the validation of the input  """
    def add_plant(self, owner: str, plant: Plant) -> None:
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def make_garden_grow(self, owner:str) -> None:
        print(f"\n{owner} is helping all plants grow ...")
        for value in self.gardens[owner]:
            value.grow()
        return

    @classmethod
    def create_garden_network() -> None:
        return

    @staticmethod
    def is_height_valid(height: int) -> bool:
        if height < 0:
            return False
        else:
            return True


if __name__ == "__main__":
    gm: GardenManager = GardenManager()
    gm.add_garden("Alice")
    gm.add_garden("Mike")
    gm.add_garden("Stalin")
    gm.add_plant("Alice", Plant("Oak Tree", 100, 50))
    gm.add_plant("Alice", FloweringPlant("Rose", 100, 50, "Red", "Blooming"))
    gm.add_plant("Alice", PrizeFlower("Sunflower", 100, 50, "Yellow", "Blooming", 10))
    gm.make_garden_grow("Alice")
    GardenManager.GardenStats.print_report("Alice", gm.gardens)
    GardenManager.GardenStats.print_general_report(gm.gardens)

    # GardenManager.GardenStats.print_all_owner(gm.gardens)