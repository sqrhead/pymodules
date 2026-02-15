from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

if __name__ == "__main__":
    print("=== DataDeck Game Engine ===")
    ge: GameEngine = GameEngine()
    fcf: FantasyCardFactory = FantasyCardFactory()
    aggst: AggressiveStrategy = AggressiveStrategy()

    ge.configure_engine(fcf, aggst)
    ge.simulate_turn()
    ge.get_engine_status()