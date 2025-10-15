import random
import math

class Slime:
    def __init__(self, player):
        self.Health = random.randint(math.round((player.MaxHealth * 0.25) - (player.MaxHealth * 0.1)), math.round((player.MaxHealth * 0.25) + (player.MaxHealth * 0.1)))
        self.attack = 2

        self.location = 'Swamp'
    
    def Jump(self):
        damage = math.round(random.uniform(self.attack - (self.attack * 0.25), self.attack + (self.attack * 0.25)))
        return damage