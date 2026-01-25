class GardenError(Exception):
    # useless since everything here is already done by Exception
    # i put it here just to remember
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"

class PlantError(GardenError):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"


class WaterError(GardenError):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"


def raise_custom_errors() -> None:
    water_tank: int = -2
    plant_status: str = "wilting"
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError . . .")
    try:
        if plant_status == "wilting":
            raise PlantError("Caught PlantError: The tomato plant is wilting!\n")
    except PlantError as pe:
        print(f"{pe}")

    print("Testing WaterError . . .")
    try:
        if water_tank < 0:
            raise WaterError("Caught WaterError: Not enough water in the tank!\n")
    except WaterError as we:
        print(f"{we}")
    print("Testing catching all garden errors...")

    try:
        if water_tank < 0:
            raise WaterError("Caught a garden error: Not enough water in the tank!")
    except GardenError as garden_error:
        print(f"{garden_error}")

    try:
        if plant_status == "wilting":
            raise PlantError("Caught a garden error: The tomato plant is wilting!\n")
    except GardenError as garden_error:
        print(f"{garden_error}")

    print("All custom error types work correctly!")

if __name__ == "__main__":
    raise_custom_errors()