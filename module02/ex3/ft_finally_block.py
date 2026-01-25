def water_plants(plant_list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant == "None":
                raise Exception("Error: cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
    except Exception as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system() -> None:
    plants: str = ["tomato", "lettuce", "carrots"]
    plants_err: str = ["tomato", "None"]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering . . .")
    water_plants(plants)
    print("\nTesting with errors  . . .")
    water_plants(plants_err)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()