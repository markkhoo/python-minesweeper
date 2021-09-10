# stuff = [["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"]]

# for i in stuff:
#     for j in i:
#         print(j, end=" ")
#     print()

# Global Variables
gameState = 0
xy = 4
bombs = 1
bombsMax = 1
bombsMin = 1


while True:
    if gameState == 0:

        print()
        print("Game Start")
        print()
        gameState += 1

    # USER chooses Map Square Size
    elif gameState == 1:
        print("Enter an integer between 4 and 40")
        xy = input("width & height of map:  ")
                
        if xy.isdigit():
            xy = int(xy)

            if xy >= 4 and xy <= 40:
                print()
                print("width & height of map: ", xy)
                print()
                gameState += 1
            else: 
                print()
                print("Invalid Input, Enter an Integer between 4 and 40")
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
                print("Invalid Input, Enter a Integer between ", bombsMin, " and ", bombsMax)
                print()

        else:
            print()
            print("Invalid Input, Enter a Integer")
            print()

    else:
        print("Map height/width: ", xy, "Number of Bombs: ", bombs)
        gameState = 0
