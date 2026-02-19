
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda power:power['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda m:m['power'] >= min_power, mages)

def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda str:'* ' + str + ' *', spells)

def mage_stats(mages: list[dict]) -> dict:
    ...


if __name__ == "__main__":

    artifact_data: list = [
        {'name': 'Staff', 'power': 100, 'type':'Wisdom'},
        {'name': 'Dagger', 'power': 25, 'type':'Poison'},
        {'name': 'Shield', 'power': 0, 'type':'Stone'},
        {'name': 'Sword', 'power': 220, 'type':'Wind'}
    ]
    print("-- Artifacts --------------------")

    # Print artifact in descending order
    for art in artifact_sorter(artifact_data):
        print(f"{art}")

    mage_data: dict = [
        {'name': 'John', 'power':130, 'element':'Fire'},
        {'name': 'Silvio Berlusconi', 'power':10, 'element':'Earth'},
        {'name': 'Mike', 'power': 3000, 'element':'Water'},
        {'name': 'Alice', 'power': 250, 'element':'Earth'},
    ]

    print("-- Mages --------------------")
    for mage in power_filter(mage_data, 250):
        print(f"{mage}")


    spell_data: list = [
        'Fireball', 'Water Splash', 'Earth Stomp', 'Wind Cut'
    ]

    print("--- Spells -------------------")

    for spell in spell_transformer(spell_data):
        print(f"{spell}")


