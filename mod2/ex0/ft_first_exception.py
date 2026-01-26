def check_temperature(temp_str: str) -> None:
    try:
        result: int = int(temp_str)
        if result < 0:
            print(f"Error: {result}°C is too cold for plants (min 0°C)")
            return
        elif result > 40:
            print(f"Error: {result}°C is too hot for plants (min 40°C)")
            return
        print(f"Temperature {result}°C is perfect for plants")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    check_temperature("25")
    print("\nTesting temperature: abc")
    check_temperature("abc")
    print("\nTesting temperature: -100")
    check_temperature("-100")
    print("\nTesting temperature: 50")
    check_temperature("50")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
