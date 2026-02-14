from ex0.Card import Card
from ex0.Card import CardType

class ArtifactCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            durability: int,
            effect: str
        ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = CardType.Artifact.name


    def play(self, game_state: dict) -> dict:
        try:
            playable = self.is_playable(game_state["mana"])
            if playable is True:
                game_state["mana"] -= self.cost
            if playable is True and game_state["playable"]:
                print("Playable: True")
            elif playable is False and game_state["playable"]:
                print("Playable: False")

            return {
                "card played": self.name,
                "mana used": self.cost,
                "effect": self.effect
            }
        except KeyError as ke:
            print(f"[ERROR]: {ke}")
            return {}
        except Exception:
            print("[ERROR] - GAME_STATE_ERROR")
            return {}

    def activate_ability(self) -> dict:
        self.durability -= 1
        if self.durability < 0:
            return {
                'result': 'Artifact expired!',
                'remaining_durability': 0
            }
        return {
            'result': self.effect,
            'remaining_durability': self.durability
        }