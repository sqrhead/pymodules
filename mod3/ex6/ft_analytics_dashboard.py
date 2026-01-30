
if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    
    users = [
        {"name":"alice", "score":2300, "active":True, "achievements": []},
        {"name":"charlie", "score":1800, "active":True, "achievements": []},
        {"name":"diana", "score":2150, "active":False, "achievements": []},
        {"name":"bob", "score":2050, "active":True, "achievements": []},
    ]
    lst_2000 = [x["name"] for x in users if x["score"] > 2000]
    doubled = [y["score"] * 2 for y in users]
    active = [j["name"] for j in users if j["active"] is True]

    print(f"High scorers (>2000): {lst_2000}")
    print(f"Scores doubled: {doubled}")
    print(f"Active players: {active}\n")

    print("=== Dict Comprehension Examples ===")
    active_player_scores: dict = {k["name"]:v["score"] for (k,v) in users if k["active"] is True}
    print(active_player_scores)
    print("=== Set Comprehension Examples ===")

    print("=== Combined Analysis ===")
