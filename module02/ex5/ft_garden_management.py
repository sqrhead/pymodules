

class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    pass


class GardenManager:

    def __init__(self, water_tank: int) -> None:
        self.garden: dict[str, Plant] = {}
        self.water_tank: int = water_tank

    def add_plant(self, name: str, water: int, sun: int) -> None:
        try:
            if name == "":
                raise ValueError("Error adding plant: Plant name cannot be empty!")
            self.garden[name] = Plant(name, water, sun)
            print(f"Added {name} successfully")
        except ValueError as ve:
            print(f"{ve}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for k in self.garden:

                self.garden[k].water = self.garden[k].water + 1
                self.water_tank = self.water_tank - 1
                if self.water_tank < 0:
                    raise GardenError("Error watering plants: Water Tank empty!")
                print(f"Watering {self.garden[k].name} - success")

        except GardenError as ge:
            print(f"{ge}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours) -> None:
        if water_level > 10:
            raise ValueError(
                f"Error checking {plant_name}: "
                f" Water level {water_level} is too high (max 10)"
            )
        elif water_level < 1 :
            raise ValueError(
                f"Error checking {plant_name}: "
                f"Water level {water_level} is too low (min 1)"
            )
        if sunlight_hours < 2:
            raise ValueError(
                f"Error checking {plant_name}: "
                f"Sun level {sunlight_hours} is too low (min 2)"
            )
        elif sunlight_hours > 12:
            raise ValueError(
                f"Error checking {plant_name}: "
                f"Sun level {sunlight_hours} is too high (max 12)"
            )
        else:
            print(
                f"{plant_name}: healthy "
                f"(water: {water_level},"
                f"sun: {sunlight_hours})"
            )

    def check_garden_health(self) -> None:
        for k in self.garden:
            plant: Plant = self.garden[k]
            try:
                self.check_plant_health(plant.name, plant.water, plant.sun)
            except ValueError as ve:
                print(f"{ve}")

    def check_garden_tank(self) -> None:
            try:
                if self.water_tank < 0:
                    raise GardenError("Caught GardenError: Not enough water in tank")
                print("No GardenErrors Found")
            except GardenError as ve:
                print(f"{ve}")
            finally:
                print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    gm: GardenManager = GardenManager(10)
    print("\nAdding plants to garden...")
    gm.add_plant("tomato", 4, 8)
    gm.add_plant("lettuce", 14, 8)
    gm.add_plant("", 12, 12)
    print("\nWatering plants...")
    gm.water_plants()
    print("\nChecking plant health...")
    gm.check_garden_health()
    print("\nTesting error recovery...")
    # gm.water_tank = -1
    gm.check_garden_tank()
    print("\nGarden management system test complete!")

    pass


if __name__ == "__main__":
    test_garden_management()