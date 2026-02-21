
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda power:power['power'], reverse=True)

# is this what they want ???
#artifact_sorter = lambda artifacts: sorted(artifacts, key=lambda power:power['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m:m['power'] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spellname:'* ' + spellname + ' *', spells))

# min() max() sum() find lower power mage, highest power mage, average power
def mage_stats(mages: list[dict]) -> dict:
    result = {}
    if not mages:
        return {}
    lmb = list(map(lambda x:x['power'], mages))
    result['max_power'] = max(lmb)
    result['min_power'] = min(lmb)
    result['avg_power'] = round(sum(lmb) / len(mages), 2) # .2f

    return result

# input not checked, remember try/except
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

    mage_data: list = [
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


    print("--- Mage Power ---------------")
    print(f"{mage_stats(mage_data)}")
