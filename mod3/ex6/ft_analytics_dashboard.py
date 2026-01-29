
if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    lst: list = ["alice", "charlie", "diana", "bob"]
    lst_2000 = [x for x in lst if x != "bob"]
    scores = [2300, 1800, 2150, 2050]
    doubled = [y * 2 for y in scores]
    active = [j for j in lst if j != "diana"]

    print(f"High scorers (>2000): {lst_2000}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active}\n")

    print("=== Dict Comprehension Examples ===")
    player_scores: dict = {
        'alice':2300,
        'bob': 1800,
        'charlie': 2150,
        'diana': 2050
    }

    print("=== Set Comprehension Examples ===")

    print("=== Combined Analysis ===")
