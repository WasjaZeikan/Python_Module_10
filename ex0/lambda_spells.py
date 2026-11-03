def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda el: el['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda el: el['power'] >= min_power,
                       mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda el: f"* {el} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    avg: float = round(sum(map(lambda el: el['power'], mages))
                       / len(mages), 2)
    return {
        'max_power': max(map(lambda el: el['power'], mages)),
        'min_power': min(map(lambda el: el['power'], mages)),
        'avg_power': avg
    }


def test_artifact_sorter(artifacts: list[dict]) -> None:
    print('Testing artifact sorter...')
    sorted_artifacts: list[dict] = artifact_sorter(artifacts)
    print('Sorted list of artifacts:')
    for art in sorted_artifacts:
        print('  Artifact', art['name'],
              'with', art['power'], 'power',
              'of', 'type:', art['type'])


def print_mage(mage: dict) -> None:
    print(' ', mage['name'],
          'with', mage['power'], 'power',
          'of', mage['element'], 'element')


def test_power_filter(mages: list[dict], min_power: int) -> None:
    print('\nTesting power filter...')
    filtered_powers: list[dict] = power_filter(mages, min_power)
    print('Mages with', min_power, 'power or higher:')
    for mage in filtered_powers:
        print_mage(mage)


def test_spell_transformer(spells: list[str]) -> None:
    print('\nTesting spell transformer...')
    print('  Spells to tranform:', spells)
    print('  Transformed spells:', spell_transformer(spells))


def test_mage_stats(mages: list[dict]) -> None:
    print('\nTesting mage stats...')
    stats: dict = mage_stats(mages)
    print('Mages stats:')
    print('  Max power =', stats['max_power'])
    print('  Min power =', stats['min_power'])
    print('  Average power =', stats['avg_power'])


def main() -> None:
    artifacts: list[dict] = [
        {'name': 'Earth Shield', 'power': 118, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 87, 'type': 'armor'},
        {'name': 'Fire Staff', 'power': 84, 'type': 'weapon'},
        {'name': 'Wind Cloak', 'power': 81, 'type': 'focus'}]
    mages: list[dict] = [
        {'name': 'Kai', 'power': 55, 'element': 'ice'},
        {'name': 'Riley', 'power': 92, 'element': 'water'},
        {'name': 'Luna', 'power': 83, 'element': 'ice'},
        {'name': 'Morgan', 'power': 91, 'element': 'shadow'},
        {'name': 'Storm', 'power': 95, 'element': 'wind'}]
    spells: list[str] = ['freeze', 'tsunami', 'tornado', 'blizzard']
    test_artifact_sorter(artifacts)
    test_spell_transformer(spells)
    print('\nMages for test:')
    for mage in mages:
        print_mage(mage)
    test_power_filter(mages, 90)
    test_mage_stats(mages)


if __name__ == '__main__':
    main()
