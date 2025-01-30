"""Pokemon battle game for CS3B Project 3."""

from electric_pokemon import ElectricType
from ice_pokemon import IceType
import random

class PokeGame:
    """Create a Pokemon deck."""
    def __init__(self):
        """Initialize the game with a deck (list) of Pokemons."""
        self.game_master = []
        self.setup()

    def setup(self):
        """Create a list of seven Pokemons."""
        self.game_master = [ElectricType("Pikachu", "Ash", 35),
                            ElectricType("Rotom", "Cynthia", 50),
                            ElectricType("Zapdos", "Lance", 90),
                            ElectricType("Miraidon", "Cynthia", 100),
                            IceType("Lapras", "Ash", 130),
                            IceType("Avalugg", "Leon", 95),
                            IceType("Alolan", "Cynthia", 90)
                            ]

    def drawPokemon(self):
        """Return a random Pokemon from the game_master deck."""
        if len(self.game_master) == 0:
            print("Game Over")
            return None
        else:
            card = random.randint(0, (len(self.game_master)-1))
            opponent = self.game_master[card]
            print("Your opponent is")
            print(opponent)
            return opponent


def display_available_types():
    """Display available Pokemon types."""
    print()
    print("Create your Pokemon from the following types:")
    print("1. Electric Type")
    print("2. Ice Type")


def create_user_pokemon():
    """Create user's pokemon based on available type."""
    user_choice = int(input("\nPlease choose your Pokemon type: "))
    name = str(input("What is your Pokemon's name: "))
    hp = int(input("What is your Pokemon's HP: "))
    match user_choice:
        case 1:
            user_pokemon = ElectricType(name, "User", hp)
        case 2:
            user_pokemon = IceType(name, "User", hp)
    print("\nYour Pokemon is:")
    print(user_pokemon)
    return user_pokemon


def main():
    """Play a game of Pokemon."""
    game = PokeGame()
    game.setup()
    opponent = game.drawPokemon()
    display_available_types()
    user_pokemon = create_user_pokemon()
    print(f"\n***{user_pokemon.name} attacks {opponent.name}")
    user_pokemon.attack(opponent)
    print(f"{opponent.name}'s HP is {opponent.hp}")


if __name__ == "__main__":
    main()


