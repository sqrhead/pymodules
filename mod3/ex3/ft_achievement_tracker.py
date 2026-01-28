
#Authorized: set(), len(), print(), union(), intersection(), difference()

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice_ach: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_ach: set =  {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_ach: set = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice_ach}")
    print(f"Player bob achievements: {bob_ach}")
    print(f"Player charlie achievements: {charlie_ach}")

    print("\n=== Achievement Analytics  ===\n")
    unique_ach: set = alice_ach.union(bob_ach, charlie_ach)
    print(f"All unique achievements: {unique_ach}")
    print(f"Total unique achievements: {len(unique_ach)}")

    common_ach: set = alice_ach.intersection(bob_ach, charlie_ach)
    print(f"\nCommon to all players: {common_ach}")
    diff_alice: set = alice_ach.difference(bob_ach, charlie_ach)
    diff_bob: set = bob_ach.difference(alice_ach, charlie_ach)
    diff_charlie: set = charlie_ach.difference(bob_ach, alice_ach)
    rare_ach: set = diff_alice.union(diff_bob, diff_charlie)
    print(f"Rare achievements (1 player): {rare_ach}\n")
    alice_bob_common: set = alice_ach.intersection(bob_ach)
    alice_bob_unq: set = alice_ach.difference(bob_ach)
    bob_alice_unq: set = bob_ach.difference(alice_ach)
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_bob_unq}")
    print(f"Bob unique: {bob_alice_unq}")
