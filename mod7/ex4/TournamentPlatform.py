from ex4.TournamentCard import TournamentCard
import random

class TournamentPlatform:
    def __init__(self):
        self.cards: list = []
        self.match_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if card is None:
            return "Card not valid"
        print(f"{card.name} ({card.id})")
        print(f"- Intefaces: {card.interfaces}")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.win} - {card.losses}")
        self.cards.append(card)
        return "Card Valid"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        cards_match: list = []
        if card1_id is None or card2_id is None:
            print("Card ID not valid")
            return {}
        # check id
        for card in self.cards:
            if card.id == card1_id:
                cards_match.append(card)
            if card.id == card2_id:
                cards_match.append(card)
        if len(cards_match) < 2:
            print("Wrong ID provided")
            return {}
        rnd_val: int = random.randint(0, 1)
        winner: int = 0
        loser: int = 0
        if rnd_val == 0:
            winner = 0
            loser = 1
        else:
            winner = 1
            loser = 0

        self.match_played += 1
        winner_card = cards_match[winner]
        loser_card = cards_match[loser]
        winner_card.calculate_rating()
        winner_card.update_wins(1)
        loser_card.update_losses(1)

        return {
            'winner': winner_card.name,
            'loser' : loser_card.name,
            'winner rating': winner_card.rating,
            'loser rating': loser_card.rating,
        }


    def get_leaderboard(self) -> list:
        self.cards.sort(key=lambda card: card.rating, reverse=True)
        return self.cards

    def generate_tournament_report(self) -> dict:
        try:
            total_rating: int = 0
            for card in self.cards:
                total_rating += card.rating

            return {
                'total cards': len(self.cards),
                'match played': self.match_played,
                'avg rating': int(total_rating / len(self.cards)),
                'platform status': 'Active'
            }
        except Exception as e:
            print("Error in generate_tournament_report[TournamentPlatform.py]")
            print(f"Error: {e}")
            return {}