from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    counter: int = 0

    def helper():
        nonlocal counter
        counter += 1
        return counter
    return helper


def spell_accumulator(initial_power: int) -> Callable:
    accumulator: int = initial_power

    def helper(power: int):
        nonlocal accumulator
        accumulator += power
        return accumulator
    return helper


def enchantment_factory(enchantment_type: str) -> Callable:
    def helper(item_name: str):
        return f"{enchantment_type} {item_name}"
    return helper


def memory_vault() -> dict[str, Callable]:
    memory: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        memory[key] = value

    def recall(key: Any) -> Any:
        return memory.get(key, "Memory not found")
    return {
        'store': store,
        'recall': recall
    }


def test_mage_counter() -> None:
    print('Testing mage counter...')
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print('counter_a call 1:', counter_a())
    print('counter_a call 2:', counter_a())
    print('counter_b call 1:', counter_b())


def test_spell_accumulator() -> None:
    print('\nTesting spell accumulator...')
    initial_power: int = 100
    for power in (20, 30):
        accumulator: Callable = spell_accumulator(initial_power)
        print('Base', initial_power,
              'add', f"{power}:", accumulator(power))


def test_enchantment_factory() -> None:
    print('\nTesting enchantment_factory...')
    flaming_factory: Callable = enchantment_factory('Flaming')
    frozen_factory: Callable = enchantment_factory('Frozen')
    print(flaming_factory('Sword'))
    print(frozen_factory('Shield'))


def test_memory_vault() -> None:
    print('\nTesting memory_vault...')
    vault: dict[str, Callable] = memory_vault()
    key: str = 'secret'
    value: int = 42
    print('Store', f"'{key}' =", value)
    vault['store'](key, value)
    print('Recall', f"'{key}':", vault['recall'](key))
    print("Recall 'unknown':", vault['recall']('unknown'))


def main() -> None:
    test_mage_counter()
    test_spell_accumulator()
    test_enchantment_factory()
    test_memory_vault()


if __name__ == '__main__':
    main()
