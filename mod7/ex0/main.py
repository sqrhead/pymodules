from ex0 import CreatureCard

if __name__ == "__main__":
    gs: dict = {
        "mana": 8,
        "creature": CreatureCard("Fire Dragon", cost=5, rarity="Legendary", attack=7, health=10),
        "target": CreatureCard("Goblin Warrior", cost=1, rarity="Normal", attack=1, health=3),
        "playable": True,
    }

    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:\n")

    print(f"CreatureCard Info:\n->{gs['creature'].get_card_info()}")
    print(f"\nPlaying {gs['creature'].name} with {gs['mana']} mana available:")
    result_play = gs["creature"].play(gs)
    print(f"Play result: {result_play}")

    print(f"\n{gs['creature'].name} attacks {gs['target'].name}:")
    result_attack = gs["creature"].attack_target(gs["target"])
    print(f"Attack result: {result_attack}")

    print(f"\nTesting insufficient mana ({gs['mana']} available):")
    result_play = gs["creature"].play(gs)

    print("\nAbstract pattern successfully demonstrated!")
