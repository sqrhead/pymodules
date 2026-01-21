def check_temperature(temp_str: str) -> int:
    try: 
        result: int = int(temp_str)
        if result < 0 :
            print(f"Error: {result}°C is too cold for plants (min 0°C)")
            return result
        if result > 40 :
            print(f"Error: {result}°C is too hot for plants (min 40°C)")
            return result
        print(f"Temperature {result}°C is perfect for plants")
        return result
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")    
        return -1

def test_temperature_input() -> None:
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: -100")
    check_temperature("-100")
    print("Testing temperature: 50")
    check_temperature("50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()