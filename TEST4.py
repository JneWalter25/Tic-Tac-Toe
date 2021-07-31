Finish, win1, win2, draw1, draw2 = True, False, False, False, False

def CheckX():
    global win1
    global draw1

    if myList2[0] == "X" and myList2[1] == "X" and myList2[2] == "X":
        win1 = True
    if myList2[3] == "x" and myList2[4] == "X" and myList2[5] == "X":
        win1 = True
    if myList2[6] == "x" and myList2[7] == "X" and myList2[8] == "X":
        win1 = True

    for i in range(3):
        if myList2[i] == "X" and myList2[i+3] == "x" and myList2[i+6] == "x":
            win1 = True

    if myList2[0] == "X" and myList2[4] == "X" and myList2[8] == "X":
        win1 = True
    elif myList2[2] == "X" and myList2[4] == "X" and myList2[6] == "X":
        win1 = True

    if not win1:
        draw1 = True


def CheckY():
    global win2
    global draw2
    for i in range(3):
        if myList2[i] == "O" and myList2[i + 3] == "O" and myList2[i + 6] == "O":
            win2 = True

    if myList2[0] == "O" and myList2[1] == "O" and myList2[2] == "O":
        win2 = True
    if myList2[3] == "O" and myList2[4] == "O" and myList2[5] == "O":
        win2 = True
    if myList2[6] == "O" and myList2[7] == "O" and myList2[8] == "O":
        win2 = True

    if myList2[0] == "O" and myList2[4] == "O" and myList2[8] == "O":
        win2 = True
    elif myList2[2] == "O" and myList2[4] == "O" and myList2[6] == "O":
        win2 = True

    if not win2:
        draw2 = True


def checkSpace():
    global Finish
    if myList2[0] == " " or myList2[1] == " " or myList2[2] == " " or myList2[3] == " " or myList2[4] == " " or myList2[5] == " " or myList2[6] == " " or myList2[7] == " " or myList2[8] == " ":
        Finish = False
    elif myList2[0] == "x" or "o" or myList2[1] == "x" or "o" or myList2[2] == "x" or "o" or myList2[3] == "x" or "o" or myList2[4] == "x" or "o" or myList2[5] == "x" or "o" or myList2[6] == "x" or "o" or myList2[7] == "x" or "o" or myList2[8] == "x" or "o":
        Finish = True

def checkFinish():
    if draw1 and draw2 and Finish:
        print("Draw")
    elif win1:
        print("X wins")
    elif win2:
        print("O wins")

xoo = False

myList2 = []

def AskXorY():
    global myList2
    myList2 = [myList[0], myList[1], myList[2], myList[3], myList[4], myList[5], myList[6], myList[7],
               myList[8]]

    while True:
        while True:
            try:
                y, x = input("Enter the coordinates: ").split()
                x = int(x)
                y = int(y)
                break
            except ValueError:
                print("You should enter numbers!")

        index = (x - 1) + (9 - (3 * y))
        if index == 6 or index == 7 or index == 8:
            index = index - 6
        elif index == 0 or index == 1 or index == 2:
            index = index + 6
        if x > 3 or y > 3:
            print("You should enter numbers!")
        elif myList2[index] == "x" or "X" and myList2[index] != "_" and myList2[index] != " ":
            print("This cell is occupied! Choose another one!")
        elif myList2[index] == "o" or "O" and myList2[index] != "_" and myList2[index] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            global xoo
            if not xoo:
                myList2[index] = "X"
                xoo = True
            else:
                myList2[index] = "O"
                xoo = False
            print("---------")
            print("|" + " " + myList2[0] + " " + myList2[1] + " " + myList2[2] + " " + "|")
            print("|" + " " + myList2[3] + " " + myList2[4] + " " + myList2[5] + " " + "|")
            print("|" + " " + myList2[6] + " " + myList2[7] + " " + myList2[8] + " " + "|")
            print("---------")
            CheckX()
            CheckY()
            checkSpace()
            if win1:
                print("X wins")
                break
            elif win2:
                print("O wins")
                break
            elif draw1 and draw2 and Finish:
                print("Draw")
                break


cells = " " * 9

myList = cells

print("---------")
print("|" + " " + myList[0] + " " + myList[1] + " " + myList[2] + " " + "|")
print("|" + " " + myList[3] + " " + myList[4] + " " + myList[5] + " " + "|")
print("|" + " " + myList[6] + " " + myList[7] + " " + myList[8] + " " + "|")
print("---------")

myList = myList.lower()

while True:
    AskXorY()
    break

