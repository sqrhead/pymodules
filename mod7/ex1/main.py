from ex1 import *

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")

    gs: dict = {
        "mana": 100,
        "deck": Deck(),
        "playable": False
    }

    try:
        print("\nBuilding deck with different card types...")
        gs['deck'].add_card(CreatureCard("Fire Dragon", 5, "Legendary", attack=7, health=10))
        gs['deck'].add_card(SpellCard("Lightning Bolt", 3, "Normal", "Deal 3 damage to target"))
        gs['deck'].add_card(ArtifactCard("Mana Crystal", 2, "Rare", 5, "Permanent +1 mana per turn"))

        print(f"Deck stats: {gs['deck'].get_deck_stats()}")

        print("\nDrawing and playing cards:\n")
        for i in range(len(gs['deck'].card_list)):
            card: Card = gs['deck'].draw_card()
            print(f"Drew: {card.name} ({card.type})")
            print(f"Play result: {card.play(gs)}")
            print()

    except Exception as e:
        print(f"[Error]: {e}")

    print("Polymorphism in action: Same interface, different card behaviors!")