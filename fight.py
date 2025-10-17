import random
import Enemies

def Fight(Player, Location): 
    print(Enemies.LocationsOfEnemies)
    Weights = [] # Chance of being picked
    NamesOfEnemies = [] # Name Of Enemy
    for a in Enemies.LocationsOfEnemies: # Find the location
        if a == Location:
            for b in Enemies.LocationsOfEnemies[a]: # get the enemies found in this location
                # print(b)
                NamesOfEnemies.append(b) # adds the enemy
                Weights.append(Enemies.LocationsOfEnemies[a][b]) # and the chance of it being there
    print(Weights)
    print(NamesOfEnemies)
    EnemyList = random.choices(NamesOfEnemies,Weights, k=1) # pick an enemy
    Enemy = EnemyList[0](Player) # create an instance of the enemy
    print(f'You encounter a {Enemy.Name} with {Enemy.Health} health')

    while Enemy.Health > 0 or Player.Health > 0: # Initiate fight loop
        for a in range(Player.EquippedWeapon.NumOfAttacks):
            AvailableAttacks = []
            print('You can use: ')
            for b in Player.EquippedWeapon.attacks.keys():
                if a == 0:
                    AvailableAttacks.append(b)
                print(b)
            Attack = input('What attack would you like to use \n')
            if Attack in AvailableAttacks:
                damage = Player.EquippedWeapon.attacks[Attack](Enemy.DodgeChance, Enemy.Name, Player)
                if damage:
                    Enemy.Health -= damage
                    print(f'You dealt {damage} damage. The {Enemy.Name} is on {Enemy.Health} health')
            else:
                while Attack not in AvailableAttacks:
                    print('Pick a valid attack')
                    Attack = input('What attack would you like to use')
                damage = Player.EquippedWeapon.attacks[Attack](Enemy.DodgeChance, Enemy.Name, Player)
                if damage:
                    Enemy.Health -= damage
                    print(f'You dealt {damage} damage. The {Enemy.Name} is on {Enemy.Health} health')
        if len(Enemy.attacks.keys()) == 1:
            EnemyAttacks = list(Enemy.attacks.keys())
            EnemyAttack = EnemyAttacks[0]
            damage = Enemy.attacks[EnemyAttack]()
            if damage:
                Player.Health -= damage
                print(f'The slime did {damage} damage to you. You are on {Player.Health} health')
        else:
            EnemyAttack = random.choice(Enemy.attacks.keys())
            damage = Enemy.attacks[EnemyAttack]()
            if damage:
                Player.Health -= damage
                print(f'The slime did {damage} damage to you. You are on {Player.Health} health')

            


    if Player.Health <= 0:
        print('You died')
    elif Enemy.Health <= 0:
        print(f'You killed the {Enemy.Name}. It dropped {Enemy.Gold} gold')
        Player.Gold += Enemy.Gold
