from ex0.Card import Card
from ex0.Card import CardType
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.type = CardType.Elite.name

    # Base
    def play(self, game_state: dict) -> dict:
        print(f"\nPlaying {self.name} ({self.type} Card)")
        return game_state

    def get_card_info(self) -> dict:
        return {
            "cap": [
                'play', 'get_card_info', 'is_playable'
            ]
        }
    # Combatable
    def attack(self, target: Card) -> dict:
        try:
            result = {
                "attacker": self.name,
                "target": target.name,
                "damage": 2,
                "combat_type": "melee"
            }
        except Exception:
            return {}
        return result

    def defend(self, incoming_damage: int) -> dict:
        if incoming_damage <= 0:
            incoming_damage = 1
        block: int = (incoming_damage + 1) /  2
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - block,
            "damage_blocked": block,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
         return {
            "cap": [
                'attack', 'defend', 'get_combat_stats'
            ]
        }

    # Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        target_res: list = []
        for x in targets:
            if isinstance(x, CreatureCard):
                target_res.append(x.name)
        return {
            "caster": self.name,
            "spell" : spell_name,
            "targets": target_res,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict:
        if amount <= 0:
            amount += 1
        return {
            "channeled": amount,
            "total_mana": amount + 2
        }

    def get_magic_stats(self) -> dict:
         return {
            "cap": [
                'cast_spell', 'channel_mana', 'get_magic_stats'
            ]
        }