import random
import math

class Sword:
    type = 'Sword'
    NumOfAttacks = 2
    attacks = []

    def Stab(self, EnemyDodgeChance, EnemyName):
        if random.randint(0, 100) > EnemyDodgeChance:
            return math.round(random.uniform(self.Attack-0.6, self.Attack+0.6))  # add damage logic here
        else:
            print(f'The {EnemyName} dodged')
    
    def __str__(self):
        return f'{self.Name} has {self.Attack} attack. It costs {self.Cost} gold'




class RustySword(Sword):
    def __init__(self, Attack):
        if Attack == 0:
            self.Attack = random.randint(1,3)
        else:
            self.Attack = Attack
        self.Name = 'Rusty Sword'
        self.Cost = (self.Attack * Sword.NumOfAttacks) * 2


