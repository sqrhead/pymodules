
# def artifact_sorter(artifacts: list[dict]) -> list[dict]:
#     return sorted(artifacts, key=lambda power:power['power'], reverse=True)

# is this what they want ???
artifact_sorter = lambda artifacts: sorted(artifacts, key=lambda power:power['power'], reverse=True)

# def power_filter(mages: list[dict], min_power: int) -> list[dict]:
#     return list(filter(lambda m:m['power'] >= min_power, mages))
power_filter = lambda mages, min_power: filter(lambda m: m['power'] >= min_power, mages)

# def spell_transformer(spells: list[str]) -> list[str]:
    # return list(map(lambda spellname:'* ' + spellname + ' *', spells))
spell_transformer = lambda spells: map(lambda spellname:'* ' + spellname + ' *', spells)

# min() max() sum() find lower power mage, highest power mage, average power
# def mage_stats(mages: list[dict]) -> dict:
#     result = {}
#     if not mages:
#         return {}
#     lmb = list(map(lambda x:x['power'], mages))
#     result['max_power'] = max(lmb)
#     result['min_power'] = min(lmb)
#     result['avg_power'] = round(sum(lmb) / len(mages), 2) # .2f

#     return result

mage_stats = lambda mages: {
    # := to create and assign in a lambda pretty cool
    'max_power': max(p := [m['power'] for m in mages]),
    'min_power': min(p),
    'avg_power': round(sum(p) / len(mages), 2)
}


# input not checked, remember try/except
if __name__ == "__main__":
    # ###################################################################
    artifact_data: list = [
        {'name': 'Staff', 'power': 100, 'type':'Wisdom'},
        {'name': 'Dagger', 'power': 25, 'type':'Poison'},
        {'name': 'Shield', 'power': 0, 'type':'Stone'},
        {'name': 'Sword', 'power': 220, 'type':'Wind'}
    ]

    print("\nTesting artifact sorter ...")
    try:
        data = artifact_sorter(artifact_data)
        len_data = len(data)
        counter = 0
        # Print artifact in descending order
        for art in data:
            print(f"{art['name']}({art['power']})", end=' ')
            counter += 1
            if counter < len_data:
                print("comes before",end=' ')
    except Exception:
        print("error: artifact_sorter wrong input date")
    # ###################################################################
    mage_data: list = [
        {'name': 'John', 'power':130, 'element':'Fire'},
        {'name': 'Silvio Berlusconi', 'power':10, 'element':'Earth'},
        {'name': 'Mike', 'power': 3000, 'element':'Water'},
        {'name': 'Alice', 'power': 250, 'element':'Earth'},
    ]

    print("\n\nTesting power filter ...")
    try:
        for mage in power_filter(mage_data, 250):
            print(f"{mage}")
    except Exception:
        print("error: power_filter wrong input data")

    # ###################################################################
    spell_data: list = [
        'Fireball', 'Water Splash', 'Earth Stomp', 'Wind Cut'
    ]

    print("\nTesting spell transformer ...")
    try:
        for spell in spell_transformer(spell_data):
            print(f"{spell}", end=" ")
    except Exception:
        print("error: spell_transformer wrong input data")
    # ###################################################################


    print("\n\nTesting mage stats ...")
    try:
        print(f"{mage_stats(mage_data)}")
    except Exception:
        print("error: mage_stats wrong input data")
