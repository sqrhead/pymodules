from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

import random


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        try:
            data: dict = self.get_supported_types()
            if isinstance(name_or_power, int):
                return CreatureCard(
                    random.randint(0, len(data["creatures"]) - 1),
                    1,
                    "Normal",
                    name_or_power,
                    5
                    )
            if isinstance(name_or_power, str):
                for name in data["creatures"]:
                    if name == name_or_power:
                        return CreatureCard(name_or_power, 1, "Normal", 1, 5)
                print(
                    "NOT VALID CREATURE NAME GIVEN: RETURNING DEFAULT OPTION"
                    )
        except Exception as e:
            print("[ERROR] in create_creature by FantasyCardFactory")
            print(f"[ERROR]: {e}")
            return CreatureCard("Goblin", 1, "Normal", 1, 5)

        return CreatureCard("Goblin", 1, "Normal", 1, 5)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        try:
            data: dict = self.get_supported_types()
            if isinstance(name_or_power, int):
                return SpellCard(
                    random.randint(0, len(data["spells"]) - 1),
                    1,
                    "Normal",
                    f"{name_or_power} damage"
                    )
            if isinstance(name_or_power, str):
                for name in data["spells"]:
                    if name == name_or_power:
                        return SpellCard(
                            name_or_power,
                            1,
                            "Normal", "1 damage"
                            )
                print(
                    "NOT VALID SPELL NAME GIVEN: RETURNING DEFAULT OPTION"
                    )
        except Exception as e:
            print("[ERROR] in create_spell by FantasyCardFactory")
            print(f"[ERROR]: {e}")
            return SpellCard("Fireball", 1, "Normal", "1 damage")

        return SpellCard("Fireball", 1, "Normal", "1 damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        try:
            data: dict = self.get_supported_types()
            if isinstance(name_or_power, int):
                art_type: list = ["mana", "wisdom", "strength", "dexterity"]
                rnd_v: int = random.randint(0, len(data["artifacts"]) - 1)
                random_artifact = data["artifacts"][rnd_v]
                type: str = ""
                for t in art_type:
                    if t in random_artifact:
                        type = t
                return ArtifactCard(
                    random_artifact,
                    1,
                    "Normal",
                    1,
                    f"+{name_or_power} {type} each turn"
                    )
            if isinstance(name_or_power, str):
                for name in data["artifacts"]:
                    if name == name_or_power:
                        return ArtifactCard(
                            name_or_power,
                            1,
                            "Normal",
                            1,
                            "+1 mana each turn"
                            )
                print(
                    "NOT VALID ARTIFACT NAME GIVEN: RETURNING DEFAULT OPTION"
                    )
        except Exception as e:
            print("[ERROR] in create_artifact by FantasyCardFactory")
            print(f"[ERROR]: {e}")
            return ArtifactCard(
                "Mana Ring",
                1,
                "Normal",
                1,
                "+1 mana each turn"
                )

        return ArtifactCard("Mana Ring", 1, "Normal", 1, "+1 mana each turn")

    def create_themed_deck(self, size: int) -> dict:
        if not isinstance(size, int):
            print("[ERROR] : INTEGER NOT PROVIDED IN 'create_themed_deck'")
            raise SystemExit
        if size <= 0:
            return {}
        if size < 3:
            print("ERROR: SIZE TOO SMALL (EXPECTED: >= 3)")
            return {}

        deck: dict = {
            "creatures": [],
            "spells": [],
            "artifacts": []
        }
        types: dict = self.get_supported_types()

        try:
            part: int = int(size / 3)
            for i in range(part):
                rnd_v = random.randint(0, len(types["creatures"]) - 1)
                deck["creatures"].append(self.create_creature(
                    types["creatures"][rnd_v]
                    ))
            for j in range(part):
                rnd_v = random.randint(0, len(types["spells"]) - 1)
                deck["spells"].append(self.create_spell(
                    types["spells"][rnd_v]
                    ))
            for k in range(part):
                rnd_v = random.randint(0, len(types["artifacts"]) - 1)
                deck["artifacts"].append(self.create_artifact(
                    types["artifacts"][rnd_v]
                    ))
        except Exception as e:
            print("[ERROR] in create_themed_deck by FantasyCardFactory")
            print(f"[ERROR]: {e}")
            return {}
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": [
                'dragon',
                'goblin',
                'orc',
                'dark elf'
                ],
            "spells": [
                'fireball',
                'lightning bolt',
                'water pistol',
                'earth fist'
                ],
            "artifacts": [
                'mana ring',
                'staff of wisdom',
                'crown of strength',
                'bow of dexterity'
                ]
        }
