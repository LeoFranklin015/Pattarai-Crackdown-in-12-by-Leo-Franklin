#TIC_TAC_TOE
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "O"
winner = None
gameRunning = True
count=0
#values for the board
def value_board():
    print("1"+" | "+"2"+" | "+"3")
    print("---------")
    print("4"+" | "+"5"+" | "+"6")
    print("---------")
    print("7"+" | "+"8"+" | "+"9")
# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input for first time
def player_first_time(board):
    global count
    inp = int(input("Select a spot 1-9: "))
    if(inp==1 or inp==5 or inp==9 or inp==3 or inp==7 ):
            board[inp-1]= currentPlayer
            count+=1
    else:
        print("YOU CAN ENTER 'O' ONLY IN DIAGONALS")
        print("TRY AGAIN!!")
11
# take player input
def playerInput(board):
    global count
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
        count+=1
    else:
        print("OOPS THE PLAYER IS ALREADY AT THE SPOT.")
        print("TRY AGAIN!!")


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"THE WINNER IS {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"THE WINNER IS {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("IT'S AN TIE!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "O":
        currentPlayer = "X"
    else:
        currentPlayer = "O"

value_board()
print("THE ABOVE MENTIONED NUMBERS ARE THE POSITION OF THE BOXES ")
while gameRunning:
    printBoard(board)
    if count==0:
        player_first_time(board)
    else:
        playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    checkIfWin(board)
    checkIfTie(board)
    