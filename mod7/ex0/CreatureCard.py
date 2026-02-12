import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        
        if self.validate(attack, health) is False:
            self.attack = 0
            self.health = 0
        else:
            self.attack = attack 
            self.health = health 

    def play(self, game_state: dict) -> dict:
        pass 

    def attack_target(self, target) -> dict: # target type ? 
        pass 

    def validate(self, attack: int, health: int) -> bool:
        if attack < 0 or health < 0:
            return False
        return True 