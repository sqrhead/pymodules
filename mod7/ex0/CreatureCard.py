from ex0.Card import Card

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
        self.type = "Creature"


    def play(self, game_state: dict) -> dict:
        try:
            if self.is_playable(game_state["mana"]) is True:
                print("Playable: True")
                game_state["mana"] -= self.cost
            else:
                print("Playable: False")
            return {
                "card played": self.name,
                "mana used": self.cost,
                "effect": "Creature summoned to the battlefield"
            }

        except Exception:
            print("[ERROR] - GAME_STATE_ERROR")
            return {}

    def is_playable(self, avaible_mana) -> bool:
        if avaible_mana > self.cost:
            return True
        else:
            return False


    def attack_target(self, target: "CreatureCard") -> dict: # target type ?
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
