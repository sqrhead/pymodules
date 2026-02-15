from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard

if __name__ == "__main__":

    print("=== DataDeck Tournament Platform ===")
    print("\nRegistering Tournament Cards...")

    tp: TournamentPlatform = TournamentPlatform()
    c1: TournamentCard = TournamentCard("Fire Dragon", 1, "Legendary")
    c2: TournamentCard = TournamentCard("Ice Wizard", 1, "SuperMegaIperRare")
    tp.register_card(c1)
    tp.register_card(c2)

    print("\nCreating tournament match...")
    print(f"Match result: {tp.create_match(c1.id, c2.id)}")

    print("\nTournament Leaderboard:")
    cards_lead: list = tp.get_leaderboard()
    index: int = 1
    for card in cards_lead:
        stats_comb = card.get_combat_stats()
        print(
            f"{index}. {card.name} - "
            f"Rating: {card.get_tournament_stats()} "
            f"({stats_comb['win']}-{stats_comb['losses']})"
            )

    print("\nPlatform Report:")
    print(f"{tp.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
