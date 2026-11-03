from collections.abc import Callable
from functools import wraps
from typing import Any
from time import sleep, perf_counter as timer


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper() -> Any:
        print('Casting', func.__name__, '...')
        time: float = timer()
        result: Any = func()
        time = timer() - time
        print(f"Spell completed in {time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(power: int) -> Any:
            if power >= min_power:
                return func(power)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def wrapper(func: Callable) -> Any:
        attempt: int = 0
        while True:
            try:
                return func()
            except Exception:
                attempt += 1
                if attempt == max_attempts:
                    return "Spell casting failed "\
                        f"after {max_attempts} attempts"
                print("Spell failed, retrying...",
                      f"(attempt {attempt}/{max_attempts})")
    return wrapper


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for ch in name:
            if not ch.isalpha() and not ch.isspace():
                return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def inner(power: int) -> Any:
            return f"Successfully cast {spell_name} with {power} power"
        return inner(power)


def test_spell_timer() -> None:
    print('Testing spell timer...')

    @spell_timer
    def fireball() -> str:
        sleep(0.5)
        return 'Fireball cast'
    print('Result:', fireball())


def test_power_validator(min_power: int, powers: list[int]) -> None:
    print('\nTesting power validator...')
    print('Minimal power:', min_power)

    @power_validator(min_power)
    def attack(_: int) -> str:
        return "Sufficient power for this spell"
    for power in powers:
        print('Casting with', power, 'power:',
              attack(power))


def test_retry_spell(max_attempts: int) -> None:
    print('\nTesting retrying spell...')
    retrying_spell: Callable = retry_spell(max_attempts)

    @retrying_spell
    def failed_spell() -> str:
        raise Exception('Fail')
    print(failed_spell)

    @retrying_spell
    def successful_spell() -> str:
        return 'Waaaaaaagh spelled !'
    print(successful_spell)


def test_MageGuild(mage_names: list[str],
                   spell_names: list[str]) -> None:
    print('\nTesting MageGuild...')
    mage_guild: MageGuild = MageGuild()
    for name in mage_names:
        print('Is', f"'{name}'", 'valid:',
              MageGuild.validate_mage_name(name))
    power: int = 8
    for spell in spell_names:
        print('Casting', f"{spell}:", mage_guild.cast_spell(spell, power))
        power += 1


def main() -> None:
    spell_names = ['heal', 'tsunami', 'earthquake', 'tornado']
    mage_names = ['A', 'Alex123', 'Jordan', 'Kai']
    test_powers = [14, 9, 19, 5]
    test_spell_timer()
    test_power_validator(14, test_powers)
    test_retry_spell(3)
    test_MageGuild(mage_names, spell_names)


if __name__ == '__main__':
    main()
