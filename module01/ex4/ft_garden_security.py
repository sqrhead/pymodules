#doppio underscore
class SecurePlant:
    def __init__(self, name: str, age: int, height: float):
        self.__name = name
        self.__age = age
        self.__height = height
        print(f"Plant created: {self.__name}")
    def get_height(self) -> float:
        return self.__height
    def get_age(self) -> int:
        return self.__age
    def get_name(self) ->str:
        return self.__name
    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height
        print(f"Heigh updated: {self.__height} [OK]")
    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__age = new_age
        print(f"Age updated: {self.__age} [OK]")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("Rose",20, 20)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-2)

    print(f"Current plant: {plant.get_name()} ({plant.get_height()}cm, {plant.get_age()} days)")