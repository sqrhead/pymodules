
if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    users = [
        {
            "name":"alice",
            "score":2300,
            "active":True,
            "achievements": ["first kill", "MVP", "treasure hunter", "level_10", "level_20"],
            "region":"central"
        },
        {
            "name":"charlie",
            "score":1800,
            "active":True,
            "achievements": ["treasure hunter", "quitter", "chest opener", "level_10", "level_20","monster_hunter", "first death"],
            "region":"north"
        },
        {
            "name":"diana",
            "score":2150,
            "active":False,
            "achievements": [],
            "region":"north"
        },
        {
            "name":"bob",
            "score":2050,
            "active":True,
            "achievements": ["level_10", "MVP", "monster_hunter"],
            "region":"east"
        },
    ]
    high_score = [x["name"] for x in users if x["score"] > 2000]
    doubled_score = [y["score"] * 2 for y in users]
    active_players = [j["name"] for j in users if j["active"] is True]

    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {doubled_score}")
    print(f"Active players: {active_players}\n")

    print("=== Dict Comprehension Examples ===")
    scores_dict: dict = {user["name"]: user["score"] for user in users if user["active"]}
    sec_dict: dict = {
        "high": len([user for user in users if user["score"] > 2100]),
        "medium": len([user for user in users if user["score"] > 2000]),
        "low": len([user for user in users if user["score"] < 200])
    }
    ach_counter: dict = {user["name"]: len(user["achievements"]) for user in users if user["active"]}
    print("Player scores: ", scores_dict)
    print("Score categories: ", sec_dict)
    print("Achievements counts: ", ach_counter)
    print("\n=== Set Comprehension Examples ===")
    unq_players: set = {user["name"] for user in users}
    unq_ach: set = {
        achievement
        for user in users
        for achievement in user["achievements"]
    }
    regions: set = {
        user["region"]
        for user in users
        if user["active"]
    }
    print("Unique players: ", unq_players)
    print("Unique achievements: ", unq_ach)
    print("Active regions", regions)


    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(unq_players)}")
    print(f"Total unique achievements: {len(unq_ach)}")
    scores: list = [user["score"] for user in users]
    average: int = 0
    for j in scores:
        average += j
    average /= len(unq_players)
    print(f"Average score: {average}")
    pl_di: dict = {user["name"]:user["score"] for user in users}
    high_player: str = ""
    high_score: int = 0
    for x in pl_di:
        if pl_di[x] > high_score:
            high_score = pl_di[x]
            high_player = x
    print(f"Top performer: {high_player} ({high_score} points, {ach_counter[high_player]} achivements)")
