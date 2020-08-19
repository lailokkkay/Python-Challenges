n = int(input())
m = int(input())

checkerBoard = []
fillState = True

def inverseBool(state):
    if state == True:
        state = False
    else:
        state = True
    return state

for i in range(n):
    row = ""
    for i in range(m):
        if fillState:
            row += ". "
            fillState = inverseBool(fillState)
        else:
            row += "* "
            fillState = inverseBool(fillState)
    checkerBoard.append([row])
    if m % 2 == 0:
        fillState = inverseBool(fillState)

for i in checkerBoard:
    print(i)
