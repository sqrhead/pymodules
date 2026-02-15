from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random

class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)
        self.id = name.upper() + "_ID"
        self.interfaces: list = ['Card', 'Combatable', 'Rankable']
        self.rating: int = random.randint(0,3000)
        self.win: int = 0
        self.losses: int = 0

    def play(self, game_state: dict) -> dict:
        try:
            if game_state["mana"] < self.cost:
                print(f"Not enought mana to play {self.name}")
                return {}
            return {
                "name": self.name,
                "rating": self.rating,
                "win": self.win,
                "losses": self.losses
            }
        except Exception as e:
            print("Error in play()[TournamentCard.py]")
            print(f"Error message: {e}")



    # Combatable
    def attack(self, target: Card) -> dict:
        try:
            return {
                "attacker": self.name,
                "defender": target.name
            }
        except Exception as e:
            print("Error in attack()[TournamentCard.py]")
            print(f"Error message: {e}")

    def defend(self, incoming_damage: int) -> dict:
        try:
            if isinstance(incoming_damage, int) is False:
                raise Exception("Input not valid, pass a integer dawg")
            return {
                "defender": self.name,
                "damage": incoming_damage
            }
        except Exception as e:
            print("Error in defend()[TournamentCard.py]")
            print(f"Error message :{e}")

    def get_combat_stats(self) -> dict:
        return {
            "win": self.win,
            "losses": self.losses
        }

    # Rankable
    def calculate_rating(self) -> int:
        self.rating += random.randint(10,20)
        return self.rating

    # wtf
    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def update_wins(self, wins: int) -> None:
        self.win += wins

    def get_tournament_stats(self) -> dict:
        return {
            "rating": self.rating
        }

    def get_rank_info(self) -> dict:
        return {
            'win': self.win,
            'losses': self.losses,
            'rating': self.rating
        }