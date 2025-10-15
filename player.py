import weapons

class Player:
    def __init__(self):
        self.MaxHealth = 20
        self.Health = 20
        
        self.BaseAttack = 1
        self.BaseDefense = 0

        self.EquippedWeapon = None
        self.WeaponsInv = []

        self.CurrentShop = []

        self.Gold = 0

        self.Level = 1
        self.RequiredXp = 100
        self.CurrentXp = 0