from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        pass

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, avaible_mana: int) -> bool:
        if avaible_mana > self.cost:
            return True
        else:
            return False
