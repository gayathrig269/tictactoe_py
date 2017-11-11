import random as r

gameBoard = []
for x in range(9):
    gameBoard.append(' ')
        

def gameCon():
    global gameBoard
    global gameActive
    gameActive = True
    for x in range(9):
        gameBoard[x] = ' '
    

def displayBoard():
    global gameBoard
    print("\n")
    print(gameBoard[0] + "  | " + gameBoard[1] + "  | " + gameBoard[2])
    print("-------------")
    print(gameBoard[3] + "  | " + gameBoard[4] + "  | " + gameBoard[5])
    print("-------------")
    print(gameBoard[6] + "  | " + gameBoard[7] + "  | " + gameBoard[8])
    print("\n")

def isEmpty(n):
    global gameBoard
    if gameBoard[n-1] == ' ':
        return True
    else:
        print("This place is already taken.")
        return False

def notValid(n):
    global gameBoard
    if n > 9 or n < 1 or not isEmpty(n):
        print("Invalid move.")
        return True
    else:
        return False

def makeMove(n, player):
    global gameBoard
    gameBoard[n-1] = player

def askPlayer(player):
    try:
        p = int(input("Player {}, enter an integer: ".format(player)))
        if notValid(p):
            askPlayer(player)
        else:
            makeMove(p, player)
        pass
    except ValueError:
        print("You didn't enter any integer. Try again.")
        askPlayer(player)
    

def checkForWinner():
    global gameActive
    if gameBoard[0] == gameBoard[1] and gameBoard[0] == gameBoard[2] and  gameBoard[0] != ' ' and gameActive:
        print("The winner is player {}".format(gameBoard[0]))
        gameActive = False
    elif gameBoard[3] == gameBoard[4] and gameBoard[3] == gameBoard[5] and gameBoard[3] != ' ' and gameActive:
        print("The winne is player {}".format(gameBoard[3]))
        gameActive = False
    elif gameBoard[6] == gameBoard[7] and gameBoard[6] == gameBoard[8] and gameBoard[6] != ' ' and gameActive:
        print("The winner is player {}".format(gameBoard[6]))
        gameActive = False
    elif gameBoard[0] == gameBoard[4] and gameBoard[8] == gameBoard[0] and gameBoard[0] != ' ' and gameActive:
        print("The winner is player {}".format(gameBoard[0]))
        gameActive = False
    elif gameBoard[2] == gameBoard[4] and gameBoard[2] == gameBoard[6] and gameBoard[2] != ' ' and gameActive:
        print("The winner is player {}".format(gameBoard[2]))
        gameActive = False
    elif gameBoard[0] == gameBoard[3] and gameBoard[0] == gameBoard[6] and gameBoard[0] != ' ' and gameActive:
        print("The winner is player {}".format(gameBoard[0]))
        gameActive = False
    elif gameBoard[1] == gameBoard[4] and gameBoard[1] == gameBoard[7] and gameBoard[1] != ' ' and gameActive:
        print("The winner is player {}".format(gameBoard[1]))
        gameActive = False
    elif gameBoard[2] == gameBoard[5] and gameBoard[2] == gameBoard[8] and gameBoard[2] != ' ' and gameActive:
        print("The winner is player {}".format(gameBoard[2]))
        gameActive = False



def start():
    global gameActive
    global counter
    counter = 0
    print("Player 'X' makes the first move. Good luck.")
    gameCon()
    displayBoard()
    counter = 0
    while gameActive:
        if (counter%2 == 0):
            askPlayer('X')
        else:
            askPlayer('O')
        displayBoard()
        counter += 1
        checkForWinner()
        if counter == 9:
            if gameActive:
                print("The match is a tie.")
                gameActive = False
    _restart()

def _isEmpty(n):
    global gameBoard
    if gameBoard[n-1] == ' ':
        return True
    else:
        return False

def _notValid(n):
    global gameBoard
    if n > 9 or n < 1 or not _isEmpty(n):
        return True
    else:
        return False
        
def randomMove(player):
    global nv
    nv = True
    a = r.randrange(1, 10)
    while _notValid(a):
        randomMove(player)
    print("The computer has made a movea at {}".format(a))
    gameBoard[a-1] = player

def _start():
    global counter
    counter = 0
    global gameActive
    gameCon()
    try:
        a = int(input("Press 1 to play with the computer; otherwise press 2... "))
        if (a == 1):
            b = int(input("Press 1 to choose 'X', otherwise press 2: "))
            r = 0
            if b == 1:
                while (gameActive):
                    if (counter % 2 == 0):
                        askPlayer('X')
                    else:
                        _ai('X', 'O')
                    displayBoard()
                    counter += 1
                    checkForWinner()
                    if counter == 9:
                        if gameActive:
                            print("The match is a tie.")
                            gameActive = False
            elif b == 2:
                while (gameActive):
                    if counter % 2 == 0:
                        _ai('O', 'X')
                    else:
                        askPlayer('O')
                    displayBoard()
                    counter += 1
                    checkForWinner()
                    if counter == 9:
                        if gameActive:
                            print("The match is a tie.")
                            gameActive = False
            else:
                print("Enter the right key. Try again.")
                _start()
        elif (a == 2):
            start()
        else:
            print("Invaid input. Try again.")
            _start()
        pass
    except ValueError:
        print("Invalid input. Try again...")
        _start()
    _restart()

def _restart():
    global gameActive
    if not gameActive:
        try:
            d = str(input("Do you want to play again? Press 'y'if 'yes' or 'n' if not...."))
            if d == 'y' or d == 'Y':
                gameActive = True
                _start()
            elif d == 'n' or d == 'N':
                print('\tExiting game')
                exit()
            else:
                print("Please enter the correct input.")
                _restart()
            pass
        except ValueError:
            print("The computer is unable to understad your input. Try again.")
            _restart()





def _checkForWinner():
    global gameActive
    if gameBoard[0] == gameBoard[1] and gameBoard[0] == gameBoard[2] and  gameBoard[0] != ' ':
        return True
    elif gameBoard[3] == gameBoard[4] and gameBoard[3] == gameBoard[5] and gameBoard[3] != ' ':
        return True
    elif gameBoard[6] == gameBoard[7] and gameBoard[6] == gameBoard[8] and gameBoard[6] != ' ':
        return True
    elif gameBoard[0] == gameBoard[4] and gameBoard[8] == gameBoard[0] and gameBoard[0] != ' ':
        return True
    elif gameBoard[2] == gameBoard[4] and gameBoard[2] == gameBoard[6] and gameBoard[2] != ' ':
        return True
    elif gameBoard[0] == gameBoard[3] and gameBoard[0] == gameBoard[6] and gameBoard[0] != ' ':
        return True
    elif gameBoard[1] == gameBoard[4] and gameBoard[1] == gameBoard[7] and gameBoard[1] != ' ':
        return True
    elif gameBoard[2] == gameBoard[5] and gameBoard[2] == gameBoard[8] and gameBoard[2] != ' ':
        return True

win1 = False

def _ai(player, antiplayer):
    global win1
    global gameBoard
    for x in range(9):
        if _isEmpty(x+1):
            gameBoard[x] = player
            if _checkForWinner():
                gameBoard[x] = antiplayer
                print("The computer has made a move at {}".format(x+1))
                win1 = True
                break
            else:
                gameBoard[x] = ' '
    if not win1:
        randomMove(antiplayer)



gameCon()
_start()

