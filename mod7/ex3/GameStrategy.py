from abc import ABC, abstractmethod

class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        ...

    def get_strategy_name(self) -> str:
        ...

    def prioritize_targets(self, available_targets: list) -> list:
        ...