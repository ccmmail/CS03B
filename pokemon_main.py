"""Pokemon battle game for CS3B Project 3."""

from electric_pokemon import ElectricType
from ice_pokemon import IceType
from psychic_pokemon import PsychicType  # by Cameron Juarez
from PokeGame import PokeGame

def display_available_types():
    """Display available Pokemon types."""
    print()
    print("Create your Pokemon from the following types:")
    print("1. Electric Type")
    print("2. Ice Type")
    print("3. Psychic Type")


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
        case 3:
            user_pokemon = PsychicType(name, "User", hp)
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
