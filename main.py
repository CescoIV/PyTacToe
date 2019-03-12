print("Welcome to PyTacToe, a 2 player python game by CescoIV")
print("------------------------------------------------------")

board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
currentPlayer = 'X'
winner = False 

def printBoard():
    print('This is the updated board: ')
    print(board[0])
    print(board[1])
    print(board[2])

def changePlayer():
    global currentPlayer
    if currentPlayer == 'X':
        print("CHANGING PLAYER")
        currentPlayer = 'O'
        print(currentPlayer)
    if currentPlayer == 'O':
        currentPlayer = 'X'

#Checks if the current player has won, uses horizontal vertical and diagonal helper methods
def hasWon():  
    h = checkHorizontals(board)
    v = checkVerticals(board)
    d = checkDiagonals(board)

    if h or v or d:
        return True
        winner = True
    else:
        return False

def checkHorizontals(board):
    if board[0][0] == currentPlayer and board[0][1] == currentPlayer and board[0][2] == currentPlayer:
        return True
    elif board[1][0] == currentPlayer and board[1][1] == currentPlayer and board[1][2] == currentPlayer:
        return True
    elif board[2][0] == currentPlayer and board[2][1] == currentPlayer and board[2][2] == currentPlayer:
        return True
    else:
        return False

def checkVerticals(board):
    if board[0][0] == currentPlayer and board[1][0] == currentPlayer and board[2][0] == currentPlayer:
        return True
    elif board[0][1] == currentPlayer and board[1][1] == currentPlayer and board[2][1] == currentPlayer:
        return True
    elif board[0][2] == currentPlayer and board[1][2] == currentPlayer and board[2][2] == currentPlayer:
        return True
    else:
        return False

def checkDiagonals(board):
    if board[0][0] == currentPlayer and board[1][1] == currentPlayer and board[2][2] == currentPlayer:
        return True
    elif board[0][2] == currentPlayer and board[1][1] == currentPlayer and board[2][0] == currentPlayer:
        return True
    else:
        return False

def placeCoordinates(r):
    print("these are your coordinates: " + r)
    if board[r[0]][r[1]] == '-':
        #place the coordinate
        board[r[0]][r[1]] = currentPlayer
        
    else:
        #if coordinate is taken, prompt a new coordinate
        print("These coordinates are taken, please insert new coordinates: ")
        a = int(input("Coordinate one: "))
        b = int(input("Coordinate two: "))
        newCoordinates = [a,b] #get new coordinates PENDING
        placeCoordinates(newCoordinates)

def takeTurn():
    global currentPlayer
    print("The current player is: " + currentPlayer)
    print("Please enter the coordinate you'd like to play, values between 0 and 2")
    a = int(input("Coordinate one: "))
    b = int(input("Coordinate two: "))

    if (a > 2 or a < 0) or (b > 2 or b < 0):
      print("These coordinates are not valid please try again")
      takeTurn()
      return

    coordinates = [a,b]
    placeCoordinates(coordinates)
    printBoard()
    winner = hasWon()

    if winner:
        print("Congratulations! " + currentPlayer + " won the game!")
        return

    # changePlayer()
    if currentPlayer == 'X':
      currentPlayer = 'O'
    elif currentPlayer == 'O':
      currentPlayer = 'X'

while winner == False:
    takeTurn()
