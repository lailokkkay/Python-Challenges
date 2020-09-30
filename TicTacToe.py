length = 3
rows = length
columns = length

player1Marker = "X"
player2Marker = "O"
empty = " "

grid = [[empty] * columns for i in range(rows)]

def PrintGrid():
    for i in range(3):
        print(grid[i])

def FindLine():
    lines = []
    diagonal1 = []
    diagonal2 = []
    for i in range(length):
        _row = []
        _column = []
        ##Diagonal Scans
        diagonal1.append(grid[i][i])
        diagonal2.append(grid[i][(length - 1) - i])
        ##Straight Scans
        for x in range(length):
            _row.append(grid[i][x])
            _column.append(grid[x][i])
        lines.append(_row)
        lines.append(_column)
    lines.append(diagonal1)
    lines.append(diagonal2)
    for i in lines:
        broken = False
        for x in range(length):
            if i[x] != i[0] or i[x] == empty:
                broken = True
        if broken != True:
            print(f"Player {i[0]} Wins!")
            return True

def PlayerMove(marker):
    rowLocation = int(input("Row : "))
    columnLocation = int(input("Colomn : "))
    while grid[rowLocation][columnLocation] != empty:
        rowLocation = int(input("Row : "))
        columnLocation = int(input("Colomn : "))

    grid[rowLocation][columnLocation] = marker

x = True
turns = 0
while FindLine() != True and turns < length * length:
    PrintGrid()
    print()
    if x:
        print(f"##Player {player1Marker}'s Turn")
        PlayerMove(player1Marker)
        x = False
    else:
        print(f"##Player {player2Marker}'s Turn")
        PlayerMove(player2Marker)
        x = True
    print()
    turns += 1
if turns >= length * length and FindLine() != True:
    print("Tie!")