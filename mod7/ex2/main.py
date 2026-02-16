from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Ability System ===")

    gs: dict = {
        "mana": 100,
        "playable": False,
        "elite": EliteCard("Arcane Warrior", 5, "Legendary"),
        "defender": CreatureCard("Enemy", 1, "None", 1, 5),
        "targets": [
            CreatureCard("Enemy1", 1, "None", 1, 5),
            CreatureCard("Enemy2", 1, "None", 1, 5),
        ],
    }
    try:
        print("\nEliteCard capabilities:")
        print(f"- Card: {gs.get('elite').get_card_info().get('cap')}")
        print(f"- Combatable: {gs.get('elite').get_combat_stats().get('cap')}")
        print(f"- Magical: {gs.get('elite').get_magic_stats().get('cap')}")

        gs.get('elite').play(gs)

        print("\nCombat phase:")
        elite: EliteCard = gs.get('elite')
        print(f"Attack result: {elite.attack(gs.get('defender'))}")
        print(f"Defence result: {elite.defend(5)}")

        print("\nMagic phase:")
        print(
            f"Spell cast: {elite.cast_spell('Fire Ball', gs.get('targets'))}"
            )
        print(f"Mana channel: {elite.channel_mana(5)}")

        print("\nMultiple interface implementation successful!")
    except Exception:
        print("[ERROR]: CMON MY MAN, STOP JOKING")
