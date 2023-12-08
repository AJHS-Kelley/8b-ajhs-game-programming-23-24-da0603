# Example Game Functions Project Damian Arnold v.0.0
import random

def revive(teamateHealth):
    if revive == True:
        teamateHealth += 100
        print("Teamate Revived!")
    elif teamateHealth > 0:
        revive == False
        print("Teamate Is Not Dead!")
        
def shootPistol(pistolAmmo):
    if shootPistol == True:   
        pistolAmmo -= 1
    elif pistolAmmo == 0:
        shootPistol == False
        print("No Ammo!")

def reloadPistol(pistolAmmo = "0"):
    if reloadPistol == True:
        pistolAmmo += 20
        print("+20 Ammo!")
    else:
        reloadPistol = False

def throwGrenade(grenades):
    if throwGrenade == True: 
        grenades -= 1
    elif grenades == 0:
        throwGrenade == False
        print("No More Grenades!")
    



# def catchBall(throwQuality, passCatchScore, weather0):
#     if throwQuality > 5.0 and passCatchScore >= 99 and weather == 'Sunny':
#         ballCaught = True
#     elif throwQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
#         ballCaught = False
#     else:
#         print('Oh, no, interception!\n')
#         ballIntercepted = True
#         return ballIntercepted
#     return ballCaught

# catchBall(4.25,107, 'Rainy')

