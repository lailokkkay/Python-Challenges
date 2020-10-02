onState = 1
offState = 0

def Nand(_input1, _input2):
    if _input1 + _input2 == onState * 2:
        out = offState
    else:
        out = onState
    return out

def Not(_input):
    return Nand(_input, _input)

def And(_input1, _input2):
    return Not(Nand(_input1, _input2))

def Xor(_input1, _input2):
    return And(Nand(_input1, _input2), Nand(Not(_input1), Not(_input2)))

def Nor(_input1, _input2):
    return And(Not(_input1), Not(_input2))

def Or(_input1, _input2):
    return Not(Nor(_input1, _input2))

def TraceTable(Gate):
    print(Gate(0,0))
    print(Gate(0,1))
    print(Gate(1,0))
    print(Gate(1,1))

print(TraceTable(Or))