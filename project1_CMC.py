"""Program to create and count objects in a list for CS03B Project 1."""

from discussion1_CMC import Books
from BoardGames_modified import BoardGame

def count_instances(data: list, *args) -> dict:
    """Count instances of objects in provided classes"""
    count = {}
    for index, obj in enumerate(data):
        print(f"item {index}: {obj.get_ID()}")
        for arg in args:
            if isinstance(obj, arg):
                count[arg.__name__] = count.get(arg.__name__, 0) + 1
    return count


def main():
    """Instantiate objects and count occurrences."""
    data = [Books("ABIN188888", "Amazing Spider-man", 26),
            Books("ABIN123456", "The Great Gatsby", 380),
            Books("ABIN455455", "Python made easy", 999),
            Books("ABIN999999", "The Gunslinger", 200),
            BoardGame("Monopoly", 2, 8, 120),
            BoardGame("Chess", 2, 2, 60),
            BoardGame("Scrabble", 2, 4, 90)
            ]

    count = count_instances(data, Books, BoardGame)
    for key in count:
        print(f'Class "{key}" has {count[key]} instances.')

if __name__ == "__main__":
    main()