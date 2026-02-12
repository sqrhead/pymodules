from ex0 import *

if __name__ == "__main__":
    game_state: dict = {
        "mana": 8,
        "creature": CreatureCard("Dragon", 5, "Legendary", 10, 100),
        "target": CreatureCard("Goblin Warrior", 1, "Normal", 1, 100)
    }

    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:\n")
    cc: CreatureCard = CreatureCard("Dragon", 5, "Legendary", 10, 100)

    print(f"CreatureCard Info:\n->{cc.get_card_info()}")
    print(f"\nPlaying {cc.name} with {game_state["mana"]} mana available:")
    result_play = cc.play(game_state=game_state)
    print(f"Play result: {result_play}")

    print(f"\n{cc.name} attacks {game_state["target"].name}:")
    result_attack = cc.attack_target(game_state["target"])
    print(f"Attack result: {result_attack}")

    print(f"\nTesting insufficient mana ({game_state["mana"]} available):")
    result_play = cc.play(game_state)

    print("Abstract pattern successfully demonstrated!")
