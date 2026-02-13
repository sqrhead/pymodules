from ex1 import * 

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")
    
    deck: Deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", attack=7, health=10))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Normal", "Deal 3 damage to target"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 5, "Permanent +1 mana per turn"))


    print("\nPolymorphism in action: Same interface, different card behaviors!")