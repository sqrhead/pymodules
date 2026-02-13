from ex0.Card import Card 
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

import random 

class Deck:

    def __init__(self) -> None:
        self.card_list: list[Card] = []

    def add_card(self, card: Card) -> None:
        try: 
            card.name 
            self.card_list.append(card)
        except Exception:
            print("[ERROR]: Card not valid")

    def remove_card(self, card_name: str) -> bool:
        for card in self.card_list:
            if card.name == card_name:
                self.card_list.remove(card)    
                return True
        return False


    def shuffle(self) -> None:
        random.shuffle(self.card_list)

    def draw_card(self) -> Card:
        card: Card = self.card_list[0]
        if self.remove_card(self.card_list[0].name):
            return card 
        return None
    
    def get_deck_stats(self) -> dict:
        total_cards: int = len(self.card_list)
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        total_mana: int = 0

        for card in self.card_list:
            total_mana += card.cost
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard): 
                spells += 1

        return {
            'total_cards': total_cards,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_costs': (total_mana / total_cards)
        }