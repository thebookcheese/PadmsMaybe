import player
import weapons

Player = player.Player() # sets the player
Player.EquippedWeapon = weapons.RustySword(2)
Player.WeaponsInv.append(weapons.RustySword(2))

def Shop(Player):
    pass

def TravellingGuy(Player):
    Locations = { # Location : Level
        'Swamp' : 1
    }
    AllowedLocations = []
    print('You can go to: \n')
    for i in Locations:
        if Player.Level >= Locations[i]:
            AllowedLocations.append(i)
            print(i + '\n')

def Town(Player):
    TravellingGuy(Player)

Town(Player)