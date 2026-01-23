def garden_operations() -> None:
    err_dict: dict [str, int] = {}
    value: int = 10
    print("Testing ValueError...")
    try:
        result: int = int("abc")
    except ValueError as ve:
        print(f"Caught ValueError: {ve}\n")
    print("Testing ZeroDivisionError ...")
    try:
        value = value / 0
    except ZeroDivisionError as zde:
        print(f"Caught ZeroDivisionError: {zde}\n")
    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt")
        file.close()
    except FileNotFoundError as fnfe:
        print(f"Caught FileNotFoundError: {fnfe}\n")
    print("Testing KeyError...")
    try:
        v: int = err_dict["missing_plant"]
    except KeyError as ke:
        print(f"Caught KeyError: {ke}\n")

    print("Testing multiple errors together...")
    try:
        value  = value / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

# EH ?
def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")

if __name__ == "__main__":
    test_error_types()