from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power),
                                  spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: \
        spell(target, power) if condition() else 'Spell fizzled'


def spell_sequence(spells: list[Callable]) -> Callable:
    def helper(target: str, power: int):
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return helper


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def tornado(target: str, power: int) -> str:
    return f"Tornado hits {target} with {power} power"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


def water(target: str, power: int) -> str:
    return f"Water spell hits {target} with {power} power"


def test_spell_combiner(target: str, power: int) -> None:
    print('Testing spell combiner...')
    new_spell: Callable = spell_combiner(tornado, heal)
    print('  Combined spell result:',
          ', '.join(new_spell(target, power)))


def test_power_amplifier(target: str, power: int) -> None:
    print('\nTesting power amplifier...')
    mega_fireball: Callable = power_amplifier(fireball, 3)
    print('  Original fireball:', fireball(target, power))
    print('  Mega fireball:', mega_fireball(target, power))


def test_conditional_caster(target: str, power: int) -> None:
    print('\nTesting conditional caster...')
    cast: Callable = conditional_caster(lambda: True, tornado)
    print("  Casting spell:", cast(target, power))
    cast = conditional_caster(lambda: False, tornado)
    print("  Casting spell:", cast(target, power))


def test_spell_sequence(target: str, power: int) -> None:
    print('\nTesting spell sequence...')
    new_spell: Callable = spell_sequence([water, tornado, fireball, heal])
    print('  Casting sequence of spells:')
    for result in new_spell(target, power):
        print('   ', result)


def main() -> None:
    test_values: list[int] = [16, 10, 16]
    test_targets: list[str] = ['Dragon', 'Goblin', 'Wizard', 'Knight']
    test_spell_combiner(test_targets[0], test_values[0])
    test_power_amplifier(test_targets[1], test_values[1])
    test_conditional_caster(test_targets[2], test_values[2])
    test_spell_sequence(test_targets[3], test_values[2])


if __name__ == '__main__':
    main()
