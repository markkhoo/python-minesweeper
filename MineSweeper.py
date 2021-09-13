# import
from random import sample

# Global Variables
gameState = 0
xy = 8
bombs = 1
bombsMax = 1
bombsMin = 1
gameMapHidden = []
gameMapShown = []
squareBomb = 'X'
squareEmptyHidden = '.'
squareEmptyShown = 'O'


def displayMapShown():
    global gameMapShown

    for i in gameMapShown:
            for j in i:
                print(j, end=" ")
            print()
    return

def displayMapHidden():
    global gameMapHidden

    for i in gameMapHidden:
            for j in i:
                print(j, end=" ")
            print()
    return

def bombAdjCount(row, col):
    global xy
    global gameMapHidden
    global squareBomb

    result = 0

    if row < 0 or col < 0 or row >= xy or col >= xy:
        result = 0
    elif gameMapHidden[row][col] == squareBomb:
        result = 1

    return result

def recursionOnEmpty(row, col):
    global xy
    global gameMapHidden
    global gameMapShown
    global squareBomb
    global squareEmptyHidden

    if row < 0 or col < 0 or row >= xy or col >= xy:
        return
    elif gameMapHidden[row][col] == squareBomb:
        return
    elif type(gameMapHidden[row][col]) is int and gameMapHidden[row][col] >= 0 and gameMapHidden[row][col] <=9:
        gameMapShown[row][col] = gameMapHidden[row][col]
        return
    elif gameMapShown[row][col] == gameMapHidden[row][col]:
        return
    elif gameMapHidden[row][col] == squareEmptyHidden:
        gameMapShown[row][col] = gameMapHidden[row][col]

        # Recursively return adjacent to the selected tile starting from the upper left going clockwise
        return (recursionOnEmpty(row - 1, col - 1), recursionOnEmpty(row - 1, col), recursionOnEmpty(row - 1, col + 1), recursionOnEmpty(row, col + 1), recursionOnEmpty(row + 1, col + 1), recursionOnEmpty(row + 1, col), recursionOnEmpty(row + 1, col - 1), recursionOnEmpty(row, col - 1))

    else:
        return

while True:
    # Reset Global Variables
    if gameState == 0:

        print()
        print("Game Start")
        print()

        xy = 8
        bombs = 4
        bombsMax = 16
        bombsMin = 4
        gameMapHidden = []
        gameMapShown = []

        gameState += 1

    # USER chooses Map Square Size
    elif gameState == 1:
        print("Enter an integer between 8 and 20")
        xy = input("width & height of map:  ")

        if xy.isdigit():
            xy = int(xy)

            if xy >= 8 and xy <= 20:
                print()
                print("width & height of map: ", xy)
                print()
                gameState += 1
            else:
                print()
                print("Invalid Input, Enter an Integer between 8 and 20")
                print()

        else:
            print()
            print("Invalid Input, Enter an Integer")
            print()

    # USER chooses Number of Bombs
    elif gameState == 2:
        bombsMin = xy // 2
        bombsMax = xy * 2
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

        mapSequence = sample([squareEmptyHidden, squareBomb], counts=[xy * xy - bombs, bombs], k=xy * xy)

        for i in range(xy):
            rowHidden = []
            rowShown = []
            for j in range(xy):
                rowHidden.append(mapSequence[i * xy + j])
                rowShown.append(squareEmptyShown)
            gameMapHidden.append(rowHidden)
            gameMapShown.append(rowShown)

        for i in range(xy):
            for j in range(xy):

                adjCount = 0

                # The following code will check adjacent tiles for bombs starting from the Upper Left going clockwise
                # Top Left
                adjCount += bombAdjCount(i - 1, j - 1)
                # Top Mid
                adjCount += bombAdjCount(i - 1, j)
                # Top Right
                adjCount += bombAdjCount(i - 1, j + 1)
                # Mid Right
                adjCount += bombAdjCount(i, j + 1)
                # Bot Right
                adjCount += bombAdjCount(i + 1, j + 1)
                # Bot Mid
                adjCount += bombAdjCount(i + 1, j)
                # Bot Left
                adjCount += bombAdjCount(i + 1, j - 1)
                # Mid Left
                adjCount += bombAdjCount(i, j - 1)

                if gameMapHidden[i][j] == squareEmptyHidden and adjCount > 0:
                    gameMapHidden[i][j] = adjCount

        gameState += 1

        print()
        print("To select a tile, enter an input as 'column, row'")
        print("(Example: 1,1 - to select top left corner)")
        print()

    # USER inputs col/row coords to play the game
    elif gameState == 4:
        print()
        # displayMapHidden()
        # print()
        displayMapShown()
        print()

        userInput = input("column,row: ")
        userInput = userInput.replace(" ", "").split(",")

        if len(userInput) < 2:
            print()
            print("Invalid input! Enter an input as 'column, row'")
            print("(Example: 1,1 - to select top left corner)")

        elif userInput[0].isdigit() and userInput[1].isdigit() and int(userInput[0]) > 0 and int(userInput[1]) > 0 and int(userInput[0]) <= xy and int(userInput[1]) <= xy:

            userInput = [int(userInput[0]) - 1, int(userInput[1]) - 1]

            selectedSquare = gameMapHidden[userInput[1]][userInput[0]]

            # When a bomb is selected
            if selectedSquare == squareBomb:
                gameMapShown[userInput[1]][userInput[0]] = selectedSquare
                print()
                displayMapShown()
                print()
                print("Hit a mine!")

                gameState += 1
            
            # When an empty tile is selected
            elif selectedSquare == squareEmptyHidden and selectedSquare != gameMapShown[userInput[1]][userInput[0]]:
                recursionOnEmpty(userInput[0], userInput[1])

            # When a number tile is selected
            elif type(selectedSquare) is int and selectedSquare >=0 and selectedSquare <= 9:
                gameMapShown[userInput[1]][userInput[0]] = gameMapHidden[userInput[1]][userInput[0]]

            else:
                pass

            # Check map for winning state
            unselectedTileCount = 0
            bombCheckAtWin = 0
            for i in range(xy):
                unselectedTileCount += gameMapShown[i].count(squareEmptyShown)
                bombCheckAtWin += gameMapShown[i].count(squareBomb)
            if bombCheckAtWin > 0:
                print()
                displayMapShown()
                print()
                print("Hit a mine!")
                gameState += 1
            elif unselectedTileCount == bombs:
                print()
                displayMapShown()
                print()
                print("You win!")
                gameState += 1

        else:
            print()
            print("Invalid input! Enter an input as 'column, row' within the bounds of the map.")
            print("(Example: 1,1 - to select top left corner)")

    else:
        
        print()
        print("Game Over")
        print()

        gameState = 0