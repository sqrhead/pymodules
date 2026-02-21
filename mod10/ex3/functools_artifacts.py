import operator
import functools
from collections.abc import Callable
from typing import Any


# spell reducer
def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case 'add':
            res = functools.reduce(operator.add, spells)
            return res
        case 'multiply':
            res = functools.reduce(operator.mul, spells)
            return res
        case 'max':
            res = functools.reduce(lambda x,y: x if x > y else y, spells)
            return res
        case 'min':
            res = functools.reduce(lambda x,y: x if x < y else y, spells)
            return res
    return None


# partial enchanter
def base_enchantment(power: int, element: str, target: str) -> str:
    return f"element: {element}, power:{power}, target: {target}"

def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) -> dict[str, Callable[[str],str]]:
    return {
        # order is important
        'fire_enchant': functools.partial(base_enchantment, 50,'fire'),
        'ice_enchant': functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(base_enchantment, 50, 'lightning'),
    }

# memoized fibonacci
@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

# spell dispatcher
def spell_dispatcher() -> Callable:

    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return f"Default behaviour for {arg}"

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return f"did a total of {damage} damage"

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return f"Enchanting with {enchantment} attribute"

    @dispatcher.register(list)
    def _(multi_cast: list) -> str:
        result = "Chaing casting: "
        for cast in multi_cast:
            result += "[" + cast + "]"
        return result

    return dispatcher



if __name__ == "__main__":

    # SPELL REDUCER
    print("\nTesting spell reducer ...")
    inp: list[int] = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(inp, 'add')}")
    print(f"Product: {spell_reducer(inp, 'multiply')}")
    print(f"Max: {spell_reducer(inp, 'max')}")
    print(f"Min: {spell_reducer(inp, 'min')}")

    # PARTIAL ENCHANTER
    print("\nTesting partial enchanter ...")
    res = partial_enchanter(base_enchantment)
    fire = res['fire_enchant']
    ice = res['ice_enchant']
    lightning = res['lightning_enchant']
    print(f"Fire: {fire('Dragon')}")
    print(f"Ice: {ice('Wyvern')}")
    print(f"Lightning: {lightning('Slime')}")

    # MEMOIZED FIBONACCI
    print("\nTesting memoized fibonacci ...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # print(f"Fib(30): {memoized_fibonacci(30)}")

    # SPELL DISPACHER
    print("\nTesting spell dispatcher ...")
    res = spell_dispatcher()
    res2 = spell_dispatcher()
    res3 = spell_dispatcher()
    res4 = spell_dispatcher()
    print(f"{res(["Fireball", "Water Splash", "Earth Stomp"])}")
    print(f"{res2('Fire')} the dagger")
    print(f"{res3(1.2)}")
    print(f"Fireball {res4(12)}")
