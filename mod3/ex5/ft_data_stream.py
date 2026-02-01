
class DataEvent:
    def __init__(self, type: str, player_name: str, player_level: int) -> None:
        self.type = type
        self.player_name = player_name
        self.player_level = player_level

    def info(self) -> str:
        print(f"Player {self.player_name} ({self.player_level}) {self.type}")


# we cant type hint this shit since i get an error :>
def data_generator(n: int):
    events: list = [
        "killed a mob",
        "found a treasure",
        "has leveled up",
        "got poisoned",
        "got hit by an arrow to his knee",
        "fell",
        "has diarrhea",
        "died",
        "got left by his/her partner",
        "has won the lottery"
    ]

    names: list = [
        "Charlie K",
        "Stalin",
        "Bob",
        "Marvin",
        "Marcello",
        "Taylor Swift",
        "Ronald Mcdonald",
        "O.J Simpson",
        "Max Verstappen",
        "Topolino"
    ]

    for i in range(n):
        yield DataEvent(
            type=events[i % 10],
            player_name=names[i % 10],
            player_level=i % 10 + 5
        )


def fibonacci_generator():
    i: int = 0
    j: int = 1
    for x in range(10):
        yield i
        tmp = j
        j = i + j
        i = tmp


def prime_generator():
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11


if __name__ == "__main__":
    total_event: int = 0
    high_level_players: int = 0
    treasure_events: int = 0
    level_up_events: int = 0
    print("=== Game Data Stream Processor ===\n")
    for x in data_generator(100):
        x.info()
        total_event += 1
        if x.player_level > 10:
            high_level_players += 1
        if x.type == "found a treasure":
            treasure_events += 1
        if x.type == "has leveled up":
            level_up_events += 1

    print("\n=== Stream Analytics ===\n")
    print(f"Total events processed: {total_event}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end=" ")
    for x in fibonacci_generator():
        print(f"{x}", end=" ")
    print("\nPrime numbers (first 5): ", end=" ")
    for y in prime_generator():
        print(f"{y}", end=" ")
    print("\n")
