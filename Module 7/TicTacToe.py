theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
turnCount = 0
win = False

while(win == False):
    printBoard(theBoard)
    print("MOVES: top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R")
    move = input("Player (" + turn + ") where would you like to move?:")
    theBoard[move] = turn
    turnCount += 1
    if(theBoard['top-L'] == turn and theBoard['top-M'] == turn and theBoard['top-R'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
    elif(theBoard['mid-L'] == turn and theBoard['mid-M'] == turn and theBoard['mid-R'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
    elif(theBoard['low-L'] == turn and theBoard['low-M'] == turn and theBoard['low-R'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
    elif(theBoard['low-L'] == turn and theBoard['mid-L'] == turn and theBoard['top-L'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
    elif(theBoard['low-M'] == turn and theBoard['mid-M'] == turn and theBoard['top-M'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
    elif(theBoard['low-R'] == turn and theBoard['mid-R'] == turn and theBoard['top-R'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
    elif(theBoard['low-L'] == turn and theBoard['mid-M'] == turn and theBoard['top-R'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
    elif(theBoard['low-R'] == turn and theBoard['mid-M'] == turn and theBoard['top-L'] == turn):
        printBoard(theBoard)
        print("Player (" + turn +") has won!")
        win = True
        
    if(turnCount == 9 and win != True):
        print("It's a draw!")
        break

    if(turn == 'X'):
        turn = 'O'
    else:
        turn = 'X'

# Now add code that allows the players to enter their moves.
# you need a for loop here and one if/else statement.
# Your code should
# print out the board at the start of each new turn
# Get the active player's move
# update the game board accordingly
# then swap the active player before moving on to the next turn
# When you run this  program, it will look something like this(see a fragment)
##
##
## | | 
##-+-+-
## | | 
##-+-+-
## | | 
##Turn for X. Move on which space?
##mid-M
## | | 
##-+-+-
## |X| 
##-+-+-
## | | 
##Turn for O. Move on which space?
##low-L
## | | 
##-+-+-
## |X| 
##-+-+-
##O| | 
##Turn for X. Move on which space?
##low-R
## | | 
##-+-+-
## |X| 
##-+-+-
##O| |X
##Turn for O. Move on which space?

