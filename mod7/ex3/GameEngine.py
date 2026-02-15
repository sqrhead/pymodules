from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
# from ex3.AggressiveStrategy import AggressiveStrategy
# from ex3.FantasyCardFactory import FantasyCardFactory


class GameEngine:
    def __init__(self):
        self.battlefield: dict = {
            "player": {
                "creatures": [],
                "life points": 100,
                "name": "Player"
            },
            "enemy": {
                "creatures": [],
                "life points": 100,
                "name": "Enemy"
            }
        }
        self.hand: list = []
        self.deck: dict = []
        self.deck_size: int = 12
        self.turn_played: int = 0
        self.total_damage: int = 0
        self.current_factory: CardFactory = None
        self.current_strategy: GameStrategy = None

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy
            ) -> None:
        try:
            self.current_factory = factory
            self.current_strategy = strategy
            print("\nConfiguring Fantasy Card Game...")
            print(f"Factory: {factory.__class__.__name__}")
            print(f"Strategy: {strategy.__class__.__name__}")
            print(f"Avaible types: {factory.get_supported_types()}")
            self.deck = factory.create_themed_deck(self.deck_size)
        except Exception:
            print("Error: wrong factory/strategy provided")
        try:
            self.hand.append(self.deck["creatures"][0])
            self.hand.append(self.deck["spells"][0])
        except Exception as e:
            print(f"Error: {e}")

    def simulate_turn(self) -> dict:
        if self.current_factory is None or self.current_strategy is None:
            print("ERROR: Failed to simulate turn ...")
            return {}
        print("\nSimulating aggressive turn...")

        print("Hand: [", end='')
        for x in self.hand:
            print(f"{x.name} ({x.cost}), ", end='')
        print("]")
        print("\nTurn execution:")
        result = self.current_strategy.execute_turn(
            self.hand, self.battlefield
            )
        try:
            self.total_damage += result["damage_dealt"]
        except Exception as e:
            print(f"Error: {e}")
        print(f"Actions: {result}")
        self.turn_played += 1
        return {
            "turn_played": True,
            "result": result
        }

    def get_engine_status(self) -> dict:
        print("\nGame Report: ")
        result = {
            'turns_simulated': self.turn_played,
            'strategy_used': self.current_strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'card_created': self.deck_size
        }
        print(f"{result}")
        return result
