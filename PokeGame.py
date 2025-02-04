"""Pokemon battle game for CS3B Project 3."""

from electric_pokemon import ElectricType
from ice_pokemon import IceType
from psychic_pokemon import PsychicType  # by Cameron Juarez
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
                            PsychicType("Mew", "Lance", 90),
                            PsychicType("Espeon", "Cynthia", 100),
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




