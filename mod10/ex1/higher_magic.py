from collections.abc import Callable

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
    def combined_spell(*args,**kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell

# Power Amplifier
def fireball_damage(damage: int) -> int:
    if isinstance(damage, int):
        return damage
    else:
        return 1

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify(*args, **kwargs) -> tuple:
        return (base_spell(*args, **kwargs), base_spell(*args, **kwargs) * multiplier)
    return amplify

# Conditional Caster
def condition_func(target: str) -> bool:
    if target is None:
        return False
    return True


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cond(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return 'Spell fizzled'
    return cond

# Spell Sequence
def spell_sequence(spells: list[Callable]) -> Callable:
    def chain_cast(*args, **kwargs) -> list[str]:
        result = []
        for spell in spells:
            result.append(spell(*args, **kwargs))
        return result
    return chain_cast

if __name__ == "__main__":

    try:
        print("\nTesting spell combiner ...")
        result = spell_combiner(spell_fireball, spell_heal)
        print(f"{result('Dragwon')}")
    except Exception:
        print("error: wrong data provided for spell combination")

    print("\nTesting power amplifier ...")
    result_ampl = power_amplifier(fireball_damage, 5)
    print(f"{result_ampl(5)}")

    print("\nTesting conditional caster ...")
    result_cond = conditional_caster(condition_func, spell_fireball)
    print(f"{result_cond('Dragwon')}")

    print("\nTesting spell sequence ...")
    result_seq = spell_sequence([
        spell_fireball,
        spell_air,
        spell_water
    ])
    for r in result_seq('Dragwon'):
        print(f"{r}")