import numpy
board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def checkRows(symbol):  
    for i in range(3):
        count = 0
        for j in range(3):
            board[i][j] == symbol
            count = count+1
        if count == 3:
            print(symbol,' won')
            return True
    return False
        
def checkColumns(symbol):
    for i in range(3):
        count = 0
        for j in range(3):
            board[j][i] == symbol
            count = count+1
        if count == 3:
            print(symbol,' won')
            return True
    return False
    
def checkDiagonals(symbol):
    count = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                board[i][j] == symbol
                count = count+1
            else:
                return False
        if count == 3:
            print(symbol,' won')
            return True
    return False
    
def won(symbol):
    return checkRows(symbol) or checkColumns(symbol) or checkDiagonals(symbol)

def place(symbol):
    print(board)
    while(1):
        row = int(input('Enter the row 1 or 2 or 3: '))
        column = int(input('Enter the column 1 or 2 or 3: '))
        if row>0 and row<4 and column>0 and column<4 and board[row-1][column-1]=='-':
            break
        else:
            print('Invalid entry')
    board[row-1][column-1] = symbol


def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
    
    if not (won(p1s)) and (won(p2s)):
        print('Its a draw')
        
play()
