from collections.abc import Callable
from functools import wraps
from typing import Any
from time import time
from time import sleep


# Spell Timer
def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any) -> Any:
        start_t = time()
        print(f'Casting {func.__name__} ...')
        sleep(.1)
        end_t = time()
        print(f'Spell completed in {round(end_t - start_t, 3)} seconds')
        return func()
    return wrapper


@spell_timer
def fireball() -> str:
    return 'fireball cast'


# Power Validator
def power_validator(min_power: int) -> Callable:
    def factory(func: Callable) -> Callable:
        @wraps(func)
        def validator(*args: Any) -> Any:
            if args[-1] >= min_power:
                return func(*args)
            else:
                return 'Insufficient power for this spell'
        return validator
    return factory


@power_validator(3)
def cast_fireball(cost: int) -> str:
    return f'Successfully casted fireball with {cost}'


# Retry Spell
def retry_spell(max_attempts: int) -> Callable:

    def deco(func: Callable) -> Callable:
        @wraps(func)
        def retries(*args: Any) -> Any:
            for n in range(max_attempts):
                try:
                    result = func(*args)
                    return result
                except Exception:
                    if n + 1 == max_attempts:
                        return 'Spell castin failed after ' +\
                            f'{max_attempts} attempts'
                    else:
                        print(
                            'Spell failed, retrying... ' +
                            f'(attempt {n + 1}/{max_attempts})'
                            )
        return retries
    return deco


@retry_spell(5)
def spell_caller(mana: int) -> str:
    if mana < 3:
        raise Exception()
    else:
        return 'Spell casted !!!'


# Mage Guild
class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for x in name:
                if x.isalpha() or x.isspace():
                    continue
                else:
                    return False
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'


if __name__ == "__main__":

    try:
        print('\nTesting spell timer')
        print(f'Result: {fireball()}')
    except Exception:
        print('error: on fireball')

    try:
        print('\nTesting power validator ...')
        print(f'{cast_fireball(5)}')
        print(f'{cast_fireball(2)}')
    except Exception:
        print('error; on power validator')

    try:
        print('\nTesting retry spell ....')
        print(f'{spell_caller(2)}')
        print(f'{spell_caller(4)}')
    except Exception:
        print('error: on retry spell')

    try:
        print('\nTesting Mage Guild ...')
        mage_guild: MageGuild = MageGuild()
        print(f'{MageGuild.validate_mage_name("Silvio Berlusconi")}')
        print(f'{MageGuild.validate_mage_name("50Cent")}')
        print(f'{mage_guild.cast_spell("Lightning", 15)}')
        print(f'{mage_guild.cast_spell("Lightning", 9)}')
    except Exception:
        print('error: on MageGuild')
