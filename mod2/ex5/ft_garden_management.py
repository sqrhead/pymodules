

class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self.name = name
        self.water = water
        self.sun = sun


class GardenError(Exception):
    pass


class WaterError(GardenError):
    pass


class PlantError(GardenError):
    pass


class GardenManager:

    def __init__(self, water_tank: int) -> None:
        self.garden: dict[str, Plant] = {}
        self.water_tank: int = water_tank

    def add_plant(self, name: str, water: int, sun: int) -> None:
        try:
            if name == "":
                raise PlantError(
                    "Error adding plant: " +
                    "Plant name cannot be empty!"
                )
            self.garden[name] = Plant(name, water, sun)
            print(f"Added {name} successfully")
        except PlantError as pe:
            print(f"{pe}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for k in self.garden:

                self.garden[k].water = self.garden[k].water + 1
                self.water_tank = self.water_tank - 1
                if self.water_tank < 0:
                    raise WaterError(
                        "Error watering plants: " +
                        "Water Tank empty!"
                    )
                print(f"Watering {self.garden[k].name} - success")

        except WaterError as we:
            print(f"{we}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name, water, sun) -> None:
        if water > 10:
            raise PlantError(
                f"Error checking {name}: "
                f" Water level {water} is too high (max 10)"
            )
        elif water < 1:
            raise PlantError(
                f"Error checking {name}: "
                f"Water level {water} is too low (min 1)"
            )
        if sun < 2:
            raise PlantError(
                f"Error checking {name}: "
                f"Sun level {sun} is too low (min 2)"
            )
        elif sun > 12:
            raise PlantError(
                f"Error checking {name}: "
                f"Sun level {sun} is too high (max 12)"
            )
        else:
            print(
                f"{name}: healthy "
                f"(water: {water},"
                f"sun: {sun})"
            )
    
    def check_garden_health(self) -> None:
        for k in self.garden:
            plant: Plant = self.garden[k]
            try:
                self.check_plant_health(plant.name, plant.water, plant.sun)
            except PlantError as pe:
                print(f"{pe}")

    def check_garden_tank(self) -> None:
        try:
            if self.water_tank < 0:
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                )
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
