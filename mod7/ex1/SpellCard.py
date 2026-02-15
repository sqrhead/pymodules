from ex0.Card import Card
from ex0.Card import CardType
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str
            ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = CardType.Spell.name

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
                "effect": self.effect_type
            }
        except KeyError as ke:
            print(f"[ERROR]: {ke}")
            return {}
        except Exception:
            print("[ERROR] - GAME_STATE_ERROR")
            return {}

    def resolve_effect(self, targets: list) -> dict:
        types: list = ["damage", "heal", "buff", "debuff"]
        fx_type: str = ""
        targets_resolved: list = []
        for fx in types:
            if fx in self.effect_type:
                fx_type = fx
        for target in targets:
            if isinstance(target, CreatureCard):
                targets_resolved.append(target)

        return {
            'fx_type': fx_type,
            'targets': targets_resolved
        }
