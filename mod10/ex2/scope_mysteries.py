from collections.abc import Callable
from typing import Any

def mage_counter() -> Callable:
    counter = 0
    def internal_counter() -> int:
        nonlocal counter
        counter += 1
        return counter
    return internal_counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def accumulate() -> int:
        nonlocal total_power
        total_power += 10
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_weapon(weapon: str) -> str:
        return f"{enchantment_type} {weapon}"
    return enchant_weapon


def memory_vault() -> dict[str, Callable]:
    result  = {}

    def store(key: Any, value: Any) -> None:
        result [key] = value

    def recall(key: Any) -> Any:
        try:
            res = result [key]
            return res
        except KeyError:
            return "Memory not found"


    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    print("\nTesting mage counter ... ")
    result = mage_counter()
    print(f"Call 1: {result()}")
    print(f"Call 2: {result()}")
    print(f"Call 3: {result()}")

    print("\nTesting spell accumulator ... ")
    result = spell_accumulator(0)
    print(f"Power Call 1: {result()}")
    print(f"Power Call 2: {result()}")
    print(f"Power Call 3: {result()}")

    print("\nTesting enchantment factor  ... ")
    result = enchantment_factory("Fire")
    result2 = enchantment_factory("Frozen")
    print(f"{result('Sword')}")
    print(f"{result2('Shield')}")

    print("\nTesting memory vault  ... ")
    result = memory_vault()
    result['store']('key', 'value')
    print(f"{result['recall']('key')}")
    print(f"{result['recall']('key2')}")
