from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        print(f"Strategy: {self.get_strategy_name()}")
        if len(hand) < 1:
            print("Actions: Empty hand - No actions")
            return {}

        mana_used: int = 0
        damage_dealt: int = 0
        # find lowest cost creature
        try:
            low_cost_cards: list = []
            for card in hand:
                if isinstance(card, CreatureCard):
                    if card.cost < 3:
                        low_cost_cards.append(card.name)
                        mana_used += card.cost
                        damage_dealt += card.attack
        except Exception:
            print("ERROR: PROBLEM AT FINDING THE LOWEST MANA CREATURE")

        try:
            targets: list = self.prioritize_targets(
                battlefield["enemy"]["creatures"]
                )
            if len(targets) < 1:
                targets += [battlefield["enemy"]["name"]]
        except Exception as e:
            print("ERROR in execute_turn by AggressiveStrategy")
            print(f"ERROR: {e}")

        return {
            'card_played': low_cost_cards,
            'mana_used': mana_used,
            'targets_attacked': targets,
            'damage_dealt': damage_dealt

        }

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        prio: list = [
            item
            for item in available_targets
            if isinstance(item, CreatureCard)
            ]
        return prio
