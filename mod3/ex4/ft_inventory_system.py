import sys


# WTF
def ret_int(number: str) -> int:
    num_str: dict[str, int] = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    result: int = 0
    for i in number:
        try:
            result = (result * 10) + num_str[i]
        except KeyError:
            print("DAWG WRONG NUMBER INPUT")
            print("INPUT EXAMPLE: <item_name>:<quantity>")
            raise SystemExit
    return result


# WTF 2 - THE RETURN
def convert_input_element(string: str) -> dict:
    str_result: str = ""
    int_result: str = ""
    trigger: bool = False
    for i in string:
        if i == ":":
            trigger = True
        elif i != ":" and trigger is False:
            str_result = str_result + i
        elif i != ":" and trigger is True:
            int_result = int_result + i
    if trigger is False:
        print("DAMN DAWG WRONG INPUT")
        print("INPUT EXAMPLE: <item_name>:<quantity>")
        raise SystemExit
    return {str_result: ret_int(int_result)}


def get_most_abudant(inventory: dict) -> list:
    key: str = ""
    value: int = 0

    for k in inventory:
        if inventory[k] > value:
            value = inventory[k]
            key = k
    return [key, value]


def get_lest_abudant(inventory: dict) -> list:
    key: str = ""
    value: int = 10000

    for k in inventory:
        if inventory[k] < value:
            value = inventory[k]
            key = k

    return [key, value]


# sword:1 potion:5 shield:2 armor:3 helmet:1
if __name__ == "__main__":
    inventory: dict[str, int] = {}
    quantities: dict[str, dict] = {
        "Abudant": {},
        "Moderate": {},
        "Scarce": {}
    }
    restock: list = []
    argv_len: int = len(sys.argv)
    index: int = 1
    if argv_len < 2:
        print("[ERROR]: No input given")
        print("[INFO] : Input Example -> <item_name>:<quantity>")
        raise SystemExit
    # create inventory
    while index < argv_len:
        inventory.update(convert_input_element(sys.argv[index]))
        index += 1

    print("=== Inventory System Analysis ===")
    total_item: int = 0
    unique_item: int = 0
    for i in inventory.values():
        total_item += i
    for j in inventory.keys():
        unique_item += 1
    print("Total items in inventory:", total_item)
    print("Unique item types: ", unique_item)

    print("\n=== Current Inventory ===")
    # try:
    for k in inventory:
        print(f"{k}: {inventory.get(k)}", end=" ")
        print("(%.1f)" % (inventory.get(k) / total_item * 100))

    print("\n=== Inventory Statistics ===")
    abundant: list = get_most_abudant(inventory)
    not_abundant: list = get_lest_abudant(inventory)
    print(f"Most  abundant: {abundant[0]} ({abundant[1]} units)")
    print(f"Least  abundant: {not_abundant[0]} ({not_abundant[1]} units)")

    # Nested dictionary
    print("\n=== Item Categories ===")
    for k in inventory:
        if inventory[k] > 9:
            quantities["Abudant"][k] = inventory[k]
        elif inventory[k] > 4:
            quantities["Moderate"][k] = inventory[k]
        else:
            quantities["Scarce"][k] = inventory[k]
    for k in quantities:
        if len(quantities[k]) < 1:
            continue
        print(f"{k}: {quantities[k]}")

    print("\n=== Management Suggestions ===")
    for k in inventory:
        if inventory[k] < 2:
            restock = restock + [k]
    print(f"Restock needed: {restock}")
    print("\n=== Dictionary Properties Demo ===")
    inv_keys: list = []
    inv_vals: list = []
    for k in inventory:
        inv_keys = inv_keys + [k]
        inv_vals = inv_vals + [inventory[k]]
    print(f"Dictionary keys: {inv_keys}")
    print(f"Dictionary values: {inv_vals}")
    try:
        inventory["sword"]
        print("Sample lookup - 'sword' in inventory: True")
    except KeyError:
        print("Sample lookup - 'sword' in inventory: False")
