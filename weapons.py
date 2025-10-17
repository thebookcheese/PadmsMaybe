import random
import math

# Rarities = Rusty, Common, Rare, Legendary
# Rusty should be able to be cleaned?
class Sword:
    def Stab(self, EnemyDodgeChance, EnemyName, Player):
        if random.randint(0, 100) > EnemyDodgeChance:
            return round(random.uniform(self.Attack-0.5, self.Attack+0.5)) + Player.BaseAttack   # add damage logic here
        else:
            print(f'The {EnemyName} dodged')
            return None
    
    type = 'Sword'
    NumOfAttacks = 2
    attacks = {
        'stab' : Stab
    }
    
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

class CommonSword(Sword):
    pass
