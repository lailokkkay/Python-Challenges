n = int(input("N = "))

board = [[0] * n for i in range(n)]

def IsSafe(board, row, col, n):
    for i in range(n):
        if board[i][col] == 1:
            return False
    _row = row
    _col = col
    for i in range(min(row,col)):
        _row -= 1
        _col -= 1
        if board[_row][_col] == 1:
            return False
    _row = row
    _col = col   
    for i in range(min(row, n-col-1)):
        _row -= 1
        _col += 1
        if board[_row][_col] == 1:
            return False
    return True

def PrintBoard(board):
    for row in range(n):
        line = ""
        for place in board[row]:
            line += f"{place} "
        print(line)

def Search(board, row, n):
    if row >= n:
        return True
    for i in range(n):
        if IsSafe(board, row, i, n):
            board[row][i] = 1
            if Search(board, row+1, n):
                return True
            board[row][i] = 0
    return False

if Search(board,0,n):
    PrintBoard(board)
else:
    print("Not possible")
