import random

class Slime:
    def __init__(self, player):
        self.Health = random.randint(player.MaxHealth * 0.25 - 1, player.MaxHealth * 0.25 + 1)