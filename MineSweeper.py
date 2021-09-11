# import
from random import sample

# Global Variables
gameState = 0
xy = 4
bombs = 1
bombsMax = 1
bombsMin = 1
gameMapHidden = []
gameMapShown = []


def displayShownMap():
    global gameMapShown

    for i in gameMapShown:
            for j in i:
                print(j, end=" ")
            print()

def displayShownHidden():
    global gameMapHidden

    for i in gameMapHidden:
            for j in i:
                print(j, end=" ")
            print()

while True:
    # Reset Global Variables
    if gameState == 0:

        print()
        print("Game Start")
        print()

        xy = 4
        bombs = 5
        bombsMax = 5
        bombsMin = 9
        gameMapHidden = []
        gameMapShown = []

        gameState += 1

    # USER chooses Map Square Size
    elif gameState == 1:
        print("Enter an integer between 4 and 20")
        xy = input("width & height of map:  ")

        if xy.isdigit():
            xy = int(xy)

            if xy >= 4 and xy <= 20:
                print()
                print("width & height of map: ", xy)
                print()
                gameState += 1
            else:
                print()
                print("Invalid Input, Enter an Integer between 4 and 20")
                print()

        else:
            print()
            print("Invalid Input, Enter an Integer")
            print()

    # USER chooses Number of Bombs
    elif gameState == 2:
        bombsMin = xy + 1
        bombsMax = xy * xy // 2 + 1
        print("Enter a integer between ", bombsMin, " and ", bombsMax)
        bombs = input("number of bombs:  ")

        if bombs.isdigit():
            bombs = int(bombs)

            if bombs >= bombsMin and bombs <= bombsMax:
                print()
                print("number of bombs: ", bombs)
                print()
                gameState += 1
            else:
                print()
                print("Invalid Input, Enter a Integer between ",
                      bombsMin, " and ", bombsMax)
                print()

        else:
            print()
            print("Invalid Input, Enter a Integer")
            print()

    # GAME Generate Map
    elif gameState == 3:

        mapSequence = sample(['.', 'X'], counts=[xy * xy - bombs, bombs], k=xy * xy)

        for i in range(xy):
            rowHidden = []
            rowShown = []
            for j in range(xy):
                rowHidden.append(mapSequence[i * xy + j])
                rowShown.append("O")
            gameMapHidden.append(rowHidden)
            gameMapShown.append(rowShown)

        gameState += 1
        print()
        print("To select a tile, enter an input as 'column, row'")
        print("(Example: 0,0 - to select top left corner)")
        print()

    # USER inputs col/row coords to play the game
    elif gameState == 4:
        print()
        displayShownMap()
        print()

        userInput = input("'column, row': ")

    else:
        
        gameState = 0
