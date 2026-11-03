from collections.abc import Callable
from typing import Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    match operation:
        case 'add':
            return functools.reduce(operator.add, spells)
        case 'multiply':
            return functools.reduce(operator.mul, spells)
        case 'max':
            return functools.reduce(lambda f, s: f if f > s else s, spells)
        case 'min':
            return functools.reduce(lambda f, s: f if f < s else s, spells)
        case _:
            raise ValueError(f"Unknown operation: '{operation}'")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'Fire': functools.partial(base_enchantment, 50, 'Fire'),
        'Ice': functools.partial(base_enchantment, 50, 'Ice'),
        'Water': functools.partial(base_enchantment, 50, 'Water')
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(_: Any) -> str:
        return 'Unknown spell type'

    @dispatch.register
    def _(dmg: int) -> str:
        return f"Damage spell: {dmg} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spells: list) -> str:
        return f"Multi-cast: {len(spells)}"

    return dispatch


def test_spell_reducer(spells: list[int]) -> None:
    print('Testing spell reducer...')
    print('Sum:', spell_reducer(spells, 'add'))
    print('Product:', spell_reducer(spells, 'multiply'))
    print('Max:', spell_reducer(spells, 'max'))
    print('Min:', spell_reducer(spells, 'min'))
    try:
        spell_reducer(spells, 'sub')
    except ValueError as err:
        print('Unknown:', err)


def test_memoized_fibonacci(tests: list[int]) -> None:
    print('\nTesting memoized fibonacci...')
    for test in tests:
        print(f'Fib({test}):', memoized_fibonacci(test))


def test_spell_dispatcher(spells: list) -> None:
    print('\nTesting spell dispatcher...')
    dispatcher: Callable[[Any], str] = spell_dispatcher()
    for spell in spells:
        print(dispatcher(spell))


def main() -> None:
    spell_powers: list[int] = [34, 34, 37, 32, 46, 49]
    fibonacci_tests: list[int] = [0, 1, 10, 20, 14, 17]
    spells: list = [42, 'fireball', [0, 1, 2], ()]
    test_spell_reducer(spell_powers)
    test_memoized_fibonacci(fibonacci_tests)
    test_spell_dispatcher(spells)


if __name__ == '__main__':
    main()
