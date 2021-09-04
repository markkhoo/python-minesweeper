# stuff = [["0","0","0","0"],["0","0","0","0"],["0","0","0","0"],["0","0","0","0"]]

# for i in stuff:
#     for j in i:
#         print(j, end=" ")
#     print()

gamestate = 0
x = 2
y = 2
bombs = 1


def checkInt(var):
    global gamestate

    if var.isdigit():
        var = int(var)
        gamestate += 1

    else:
        print("enter an integer")

    return


while True:
    if gamestate == 0:

        # place holder line
        print()
        print("Game Start")
        print()
        gamestate += 1

    elif gamestate == 1:
        x = input("width of map:  ")
        print("width of map: ", x)
        checkInt(x,)

    elif gamestate == 2:
        y = input("height of map:  ")
        print("height of map: ", y)
        checkInt(y)

    elif gamestate == 3:
        bombs = input("number of bombs:  ")
        print("number of bombs: ", bombs)
        checkInt(bombs)

    else:
        print("height: ", y, "width: ", x, "bombs: ", bombs)
        gamestate = 0
