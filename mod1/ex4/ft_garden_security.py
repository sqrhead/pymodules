
class SecurePlant:
    """ SecurePlant class """
    def __init__(self, name: str, age: int, height: float):
        """ Initializer """
        self.__name = name
        self.__age = age
        self.__height = height
        print(f"Plant created: {self.__name}")

    def get_height(self) -> float:
        """ Getter for height """
        return self.__height

    def get_age(self) -> int:
        """ Getter for age """
        return self.__age

    def get_name(self) -> str:
        """ Getter for name """
        return self.__name

    def set_height(self, new_height: float) -> None:
        """ Setter for height """
        if new_height < 0:
            print(
                f"\nInvalid operation attempted: "
                f"height {new_height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            return
        self.__height = new_height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        """ Setter for age """
        if new_age < 0:
            print(f"\nInvalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = new_age
        print(f"Age updated: {self.__age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant: SecurePlant = SecurePlant("Rose", 20, 20)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print(
        f"\nCurrent plant: {plant.get_name()}"
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )
