import random
import Enemies

def Fight(Player, Location): 
    print(Enemies.LocationsOfEnemies)
    Weights = [] # Chance of being picked
    NamesOfEnemies = [] # Name Of Enemy
    for a in Enemies.LocationsOfEnemies: # Find the location
        if a == Location:
            for b in Enemies.LocationsOfEnemies[a]: # get the enemies
                print(b)
                NamesOfEnemies.append(b)
                Weights.append(Enemies.LocationsOfEnemies[a][b])
    print(Weights)
    print(NamesOfEnemies)
    EnemyList = random.choices(NamesOfEnemies,Weights, k=1)
    Enemy = EnemyList[0](Player)
    print(Enemy.Health)

    while Enemy.Health > 0 or Player.Health > 0:
        AvailableAttacks = []
        for a in range(Player.EquippedWeapon.NumOfAttacks):
            print('You can use: ')
            for b in Player.EquippedWeapon.attacks.keys():
                if a == 0:
                    AvailableAttacks.append(b)
                print(b)
            Attack = input('What attack would you like to use')
            if Attack in AvailableAttacks:
                Player.EquippedWeapon.attacks[Attack]
            else:
                while Attack not in AvailableAttacks:
                    print('Pick a valid attack')
                    Attack = input('What attack would you like to use')
                Player.EquippedWeapon.attacks[Attack]
            

            


    if Player.Health <= 0:
        print('You died')
    elif Enemy.Health <= 0:
        print(f'You killed the {Enemy.Name}. It dropped {Enemy.Gold} gold')
        Player.Gold += Enemy.Gold
