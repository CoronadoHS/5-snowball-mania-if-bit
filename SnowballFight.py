''' 
    Name: Snowball-Mania
    Author: izaiah fabela
    Date: 12/5/2025
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

import random
import time


def printIntro():
    '''
    ' Param: none
    ' 
    ' Print a welcome message to the user
    ' 
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("❄️  Welcome to Snowball Mania!❄️")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def getNames():
    '''
    ' Param: none
    ' 
    ' Create a list to hold player names.
    ' Ask the user for their name.  Store it in a variable and add it to the player list.
    ' Print instructions for the user to add more players and to type "DONE" when finished.
    ' Read in the first additional player name.
    ' While the user hasn't typed "DONE", add the new name to the player list and prompt for the next name
    ' After the user is finished entering names, print a "Time to play!" message
    '
    ' Return: the list of player names
    ' 
    '''
    playerlist = []
    myname = input("name please ")
    playerlist.append(myname)
    print( "add more players type done when done")
    input()
    nextname = input()
    while (nextname != "done"):
        playerlist.append (nextname)
        nextname = input()
    print("get ready :)")
    return playerlist

def getThrower(players):
    '''
    ' Param: players (list of player names)
    '
    ' Return a randomly chosen player name to be the next thrower.
    '
    ' Return: player name
    '''
    thrower = random.choice(players)
    return thrower 
    
def getVictim(players, t):
    '''
    ' Param: players (list of player names), t (the thrower for this round)
    ' 
    ' Select a random player to be the next victim.  
    ' While the victim is the same player as the thrower, randomly select a new victim from the list.
    ' Return the victim's name.
    '
    ' Return: victim's name
    '''
    vitctim = random.choice(players)
    while (vitctim == t):
        vitctim = random.choice(players)
    return vitctim 
        




def getHitResult():
    '''
    ' Param: none
    ' 
    ' Generate a random number between 1 and 10
    ' If the number is greater than ___, return True
    ' Else, return False
    '
    ' Return: Boolean representing whether or not the snowball hit
    '''
    numthrower = random.randint(1 , 10)
    numvitctim = random.randint(1 , 10)
    if(numthrower >= numvitctim):
        return True
    else:
        return False 

def playSnowballFight(players):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    
   
    

    while (len(players) > 1 ):
        thrower = getThrower(players)
        vitctim = getVictim(players , thrower)
        hitresult = getHitResult() 

        if (hitresult == True):
            koresult = random.randint(1,2) # 1=ko 2=no ko 
            if (koresult == 1):
                print(thrower + " throws at " + vitctim + " and hits but is not out")
            else: 
                print(thrower + " takes out " + vitctim + " - " + vitctim + " is out")
                players.remove(vitctim)
        else:
            print(thrower + " throws at " + vitctim + "but misses")
        time.sleep(3)

def printOutro(winner):
    '''
    ' Param: name of the winner
    ' 
    ' Print a congratulatory message naming the winner
    '
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("All hail " + winner + ", the Ultimate Student/Snowball Wizard!")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def runProgram():
    '''
    ' Param: none
    ' 
    ' Call the method that will print the intro messages
    ' Call the method that will return a list of player names.  Save the list in a variable.
    ' Call the method that will simulate the snowball fight
    ' Call the method that will print the outro messagees
    '
    ' Return: none
    '''
    printIntro()
    testplayers = getNames() 
    playSnowballFight(testplayers)
    printOutro(testplayers[0])
    



runProgram()
# testthrower = getThrower(testplayers)
# testvitctim = getVictim(testplayers , testthrower)
# testhit = getHitResult()

# # successful hit
# if (testhit == True):
#     print(testthrower + " throws at " + testvitctim + " -hit")
# # miss
# else:
#     print(testthrower + " throws at " + testvitctim + " -miss")
