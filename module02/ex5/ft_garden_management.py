

class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class GardenManager:

    def __init__(self):
        self.garden: dict[str, Plant] = {}
        self.water_tank: int = 20

    def add_plant(self, name: str, water: int, sun: int) -> None:
        try:
            if name == "":
                raise ValueError("Error adding plant: Plant name canot be empty!")
            self.garden[name] = Plant(name, water, sun)

        except ValueError as ve:
            print(f"{ve}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            if water_tank < 0:
                raise ValueError("Error watering plants: Water Tank empty!")
            for k in self.garden:
                print(f"Watering {self.garden[k].name} - success")
                self.garden[k].water = self.garden[k].water + 1
        except ValueError as ve:
            print(f"{ve}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_healt(plant) -> None:

        pass

if __name__ == "__main__":
    pass