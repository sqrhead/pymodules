from collections.abc import Callable
from typing import Any


# Combination Spells
def spell_fireball(target: str) -> str:
    return f"Fireball hits {target}"


def spell_air(target: str) -> str:
    return f"Air cut hits {target}"


def spell_water(target: str) -> str:
    return f"Water splash hit {target}"


def spell_heal(target: str) -> str:
    return f"Heal {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise Exception("error: spell1/spell2 not functions")

    def combined_spell(*args: Any) -> tuple:
        return (spell1(*args), spell2(*args))
    return combined_spell


# Power Amplifier
def fireball_damage(damage: int) -> int:
    if isinstance(damage, int):
        return damage
    else:
        return 1


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise Exception("error: base_spell not function")

    def amplify(*args: Any) -> tuple:
        return (base_spell(*args), base_spell(*args) * multiplier)
    return amplify


# Conditional Caster
def condition_func(target: str) -> bool:
    if target is None:
        return False
    return True


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition):
        raise Exception("error: condition not function")

    def cond(*args: Any) -> str:
        if condition(*args):
            return spell(*args)
        else:
            return 'Spell fizzled'
    return cond


# Spell Sequence
def spell_sequence(spells: list[Callable]) -> Callable:
    def chain_cast(*args: Any) -> list[str]:
        result = []
        for spell in spells:
            if not callable(spell):
                raise Exception(
                    "spells contain something more than a callable"
                    )
            result.append(spell(*args))
        return result
    return chain_cast


if __name__ == "__main__":

    try:
        print("\nTesting spell combiner ...")
        result = spell_combiner(spell_fireball, spell_heal)
        print(
            f"Combined spell result : {result('Dragwon')[0]}, "
            f"{result('Dragwon')[1]}"
            )
    except Exception as e:
        print("error: wrong data provided for spell combination")
        print(f'{e}')

    try:
        print("\nTesting power amplifier ...")
        result_ampl = power_amplifier(fireball_damage, 5)
        tmp = result_ampl(5)
        print(f"Original: {tmp[0]}, Amplified: {tmp[1]}")
    except Exception as e:
        print('error: wrong data provided for power amplifier')
        print(f'{e}')

    try:
        print("\nTesting conditional caster ...")
        result_cond = conditional_caster(condition_func, spell_fireball)
        print(f"{result_cond('Dragwon')}")
    except Exception as e:
        print('error: wrong data provided for conditional caster')
        print(f'{e}')

    try:
        print("\nTesting spell sequence ...")
        result_seq = spell_sequence([
            spell_fireball,
            spell_air,
            spell_water
        ])
        for r in result_seq('Dragwon'):
            print(f"{r}")
    except Exception as e:
        print('error: wrong data provided for spell sequence')
        print(f'{e}')
