import player
import weapons
import fight

Player = player.Player() # sets the player
Player.EquippedWeapon = weapons.RustySword(2) # give the player a sword 
Player.WeaponsInv.append(weapons.RustySword(2)) # add it to the weapons inventory

def Shop(Player): # shop
    pass

def TravellingGuy(Player):
    Locations = { # Location : Level
        'Swamp' : 1
    }
    AllowedLocations = []
    print('You can go to: \n') # says where you can go
    for i in Locations:
        if Player.Level >= Locations[i]:
            AllowedLocations.append(i)
            print(i + '\n')
    Location = input('Where do you want to go \n')
    if Location not in AllowedLocations:
        while Location not in AllowedLocations:
            print('Pick new Location')
            Location = input('Where do you want to go \n')
    else:
        fight.Fight(Player)


def Town(Player):
    TravellingGuy(Player)

Town(Player)