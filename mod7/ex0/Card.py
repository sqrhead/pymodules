from abc import ABC, abstractmethod
from enum import Enum

class CardType(Enum):
    Nothing = 0
    Creature = 1


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

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
