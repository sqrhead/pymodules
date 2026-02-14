from ex0.Card import Card
from ex0.Card import CardType

class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0:
            self.attack = 1
        else:
            self.attack = attack
        if health < 0:
            self.health = 1
        else:
            self.health = health
        self.type: CardType = CardType.Creature.name


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
                "effect": "Creature summoned to the battlefield"
            }
        except KeyError as ke:
            print(f"[ERROR]: {ke}")
            return {}
        except Exception:
            print("[ERROR] - GAME_STATE_ERROR")
            return {}


    def attack_target(self, target: Card) -> dict:
        resolved = False
        target.health -= self.attack
        if target.health <= 0:
            resolved = True
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": resolved
        }


    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        }
