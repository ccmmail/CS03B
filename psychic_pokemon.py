### A Psychic type Pokémon

from pokemon import *

class PsychicType(Pokemon):
    
    basic_attack = 'Psychic Shift'

    def __init__(self, name, trainer, hp = None):
        super().__init__(name, trainer)
        if hp != None:
            self.hp = hp

    def __str__(self):
        ret_str = f'Pokemon:{self.name}\t Trainer:{self.trainer}\n'\
                  f'Level:{self.level}\t HP:{self.hp}'
        return ret_str

    def attack(self, other):
        """Modified attack method for Psychic Type"""
        # check to see if weak against (need to divide damage by 2)
        if isinstance(other, BugType) or isinstance(other, GhostType)\
                or isinstance(other, DarkType):
            self.damage = Pokemon.damage / 2
        # check to see if strong against (need to multipy damage by 2)
        elif isinstance(other, FightingType) or isinstance(other, PoisonType):
            self.damage = Pokemon.damage * 2
        # run attack from Pokémon parent class
        super().attack(other)
        # probability of paralysis is 100% for Psychic Type Pokémon
        other.paralyzed = True
        print(f'{other.name} is paralyzed!')
        # reset damage to original
        self.damage = Pokemon.damage

# placeholder classes for pokemons that Ice type is strong or weak against
class BugType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class GhostType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class DarkType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class FightingType(Pokemon):
    """Create placeholder types of pokemon."""
    pass

class PoisonType(Pokemon):
    """Create placeholder types of pokemon."""
    pass
