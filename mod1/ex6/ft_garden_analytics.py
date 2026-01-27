

class Plant:
    """ Basic Plant class"""
    def __init__(self, name, age, height):
        """ Initializer """
        self.name = name
        self.age = age
        self.height = height
        self.type: str = "Plant"

    def grow(self) -> None:
        """ Grow function to make grow the plants"""
        self.height = self.height + 1
        print(f"{self.name} grew 1cm")

    def log(self) -> None:
        """ Function to log required for the final format """
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """ FloweringPlant class  """

    def __init__(self, name, age, height, color, status):
        """ Initializer """
        super().__init__(name, age, height)
        self.color = color
        self.status = status
        self.type: str = "FloweringPlant"

    def log(self) -> None:
        """ Function to log required for the final format """
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({self.status})"
        )


class PrizeFlower(FloweringPlant):
    """ PrizeFlower class  """

    def __init__(self, name, age, height, color, status, prize_points):
        """ Initializer """
        super().__init__(name, age, height, color, status)
        self.prize_points: int = prize_points
        self.type: str = "PrizeFlower"

    def log(self) -> None:
        """ Function to log required for the final format """
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({self.status}), "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    """ GardenManager class used to manage a gardens duh"""

    def __init__(self):
        """ Constructor """
        print("=== Garden Management System Demo ===\n")
        self.gardens: dict[str, list[Plant]] = {}
        self.scores: dict[str, int] = {}
        self.gardens_number: int = 0
        self.growth_counter: int = 0
        self.regular_counter: int = 0
        self.flowering_counter: int = 0
        self.prizeflower_counter: int = 0

    class GardenStats:
        """ GardenStats nested class used as a helper, to display infos"""

        @staticmethod
        def print_report(owner: str, gardens: dict) -> None:
            """ Function to print single report  """
            print(f"\n=== {owner}'s Garden Report ===")
            print("Plants in garden:")
            for value in gardens[owner]:
                value.log()

        @staticmethod
        def get_score(owner: str, gardens: dict) -> int:
            """ Function to get the scores"""
            score: int = 0
            for value in gardens[owner]:
                if value.type == "PrizeFlower":
                    score += value.prize_points
            return score

        @staticmethod
        def print_general_report(gm_instance) -> None:
            """ Function to print the rest of the format """
            print(
                f"\nPlants added: {gm_instance.gardens_number},"
                f"Total growth: {gm_instance.growth_counter}cm"
            )
            print(
                f"Plant types: {gm_instance.regular_counter} regular, "
                f"{gm_instance.flowering_counter} flowering, "
                f"{gm_instance.prizeflower_counter} prize flowers\n"
            )

            if gm_instance.get_height_validation(gm_instance.gardens) is True:
                print("Height validation test: True")
            else:
                print("Height validation test: False")
            gm_instance.fill_scores()
            print("Garden scores -", end=' ')
            for k in gm_instance.scores:
                print(f"{k}: {gm_instance.scores[k]}  ", end=' ')
            # print("\n")
            print(f"\nTotal garden managed: {gm_instance.gardens_number}")

    def get_height_validation(self, gardens: dict[str, list[Plant]]) -> bool:
        """ Function to check all the height of the plants"""
        for key in gardens:
            for value in gardens[key]:
                if self.is_height_valid(value.height) is False:
                    return False
        return True

    def add_garden(self, owner: str) -> None:
        """ Function to add a garden,
        it just creates a empty list in the dict"""
        for key in self.gardens:
            if key == owner:
                print("Error: This name is already used")
                return
        self.gardens[owner] = []
        self.gardens_number = self.gardens_number + 1

    def fill_scores(self) -> None:
        """ Function to get the scores of all the garden owners"""
        for k in self.gardens:
            self.scores[k] = 0
            for v in self.gardens[k]:
                if v.type == "PrizeFlower":
                    self.scores[k] += v.prize_points

    def add_plant(self, owner: str, plant: Plant) -> None:
        """ Function to add a plant to a garden """
        for k in self.gardens:
            if k == owner:
                self.gardens[owner] = self.gardens[owner] + [plant]
                print(f"Added {plant.name} to {owner}'s garden")
                if plant.type == "Plant":
                    self.regular_counter = self.regular_counter + 1
                elif plant.type == "FloweringPlant":
                    self.flowering_counter = self.flowering_counter + 1
                elif plant.type == "PrizeFlower":
                    self.prizeflower_counter = self.prizeflower_counter + 1

    def make_garden_grow(self, owner: str) -> None:
        """ Function to count total gardens"""
        print(f"\n{owner} is helping all plants grow ...")
        for value in self.gardens[owner]:
            value.grow()
            self.growth_counter = self.growth_counter + 1
        return

    @classmethod
    def create_garden_network(cls):
        """ @classmethod Function required by the subject """
        instance = cls()
        return instance

    @staticmethod
    def is_height_valid(height: int) -> bool:
        """ Function to check for height in the final format"""
        if height < 0:
            return False
        else:
            return True


if __name__ == "__main__":
    gm: GardenManager = GardenManager.create_garden_network()
    gm.add_garden("Alice")
    gm.add_garden("Mike")
    gm.add_garden("Stalin")
    gm.add_plant("Alice", Plant("Oak Tree", 100, 50))
    gm.add_plant("Alice", FloweringPlant("Rose", 100, 59, "Red", "Blooming"))
    gm.add_plant(
        "Alice",
        PrizeFlower(
            "Sunflower", 100, 50, "Yellow", "Blooming", 10
        )
    )
    gm.add_plant("Hitler", Plant("Oak Tree", 500, 80))
    gm.make_garden_grow("Alice")
    GardenManager.GardenStats.print_report("Alice", gm.gardens)
    GardenManager.GardenStats.print_general_report(gm)
