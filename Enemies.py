import random
import math

class Slime:
    def __init__(self, player):
        self.Health = random.randint(round((player.MaxHealth * 0.25) - (player.MaxHealth * 0.1)), round((player.MaxHealth * 0.25) + (player.MaxHealth * 0.1))) # Works out the health of the slime based on the health of the player
        self.Attack = 2
        self.Gold = random.randint(1, 5)
        self.Name = 'Slime'
        self.DodgeChance = 3
    
    def Jump(self):
        damage = round(random.uniform(self.attack - (self.attack * 0.25), self.attack + (self.attack * 0.25)))
        return damage
    

LocationsOfEnemies = {
    'Swamp' : {Slime : 100}
}