# Example Game Functions Project Damian Arnold v.0.0
import random

def revive(teamateHealth):
    if revive == True:
        teamateHealth += 100
        print("Teamate revived!")
        
def shootPistol(pistolAmmo):
    if shootPistol == True:   
        pistolAmmo -= 1

def reloadPistol(pistolAmmo = "0"):
    if pistolAmmo == 0:
        pistolAmmo += 20
        print("+20 Ammo!")
    else:
        reloadPistol = False

def throwGrenade(grenades):
    if throwGrenade == True:
        grenades -= 1
    elif grenades == 0:
        throwGrenade == False
        print("No more grenades!")
    



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

