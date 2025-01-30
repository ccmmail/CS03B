from pokemon import Pokemon

class ElectricType(Pokemon):

    basic_attack = "thunder shock"
    prob = 0.1

    def __init__(self, name, trainer, hp = None):
        super().__init__(name, trainer)
        if hp != None:
            self.hp = hp

    def __str__(self):
        ret_str = "Pokemon name: {}\t Trainer: {}\n"\
                  "Level: {}\tHP: {}".format(self.name, self.trainer, self.level, self.hp)
        return ret_str

    def __repr__(self):
        ret_str = "ElectricType({})".format(self.name)
        return ret_str

    def attack(self, other):
        #check to see if weak against (need to divide damage by 2)
        if isinstance(other, GrassType) or isinstance(other, ElectricType):
            self.damage = Pokemon.damage/2
        #check to see if strong against (need to multipy damage by 2)
        elif isinstance(other, FlyingType) or isinstance(other, WaterType):
            self.damage = Pokemon.damage*2
        # run attack
        super().attack(other)
        # check to see if pokemon paralyzed
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, "is paralyzed!")
        # reset damage to original
        self.damage = Pokemon.damage


        
