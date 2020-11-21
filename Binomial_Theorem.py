print("(coefficientX(x)^exponentX + coefficientY(y)^exponentY)^exponent")

coefficientX = int(input("Coefficient of X : "))
exponentX = int(input("Exponent of X : "))
coefficientY = int(input("Coefficient of Y : "))
exponentY = int(input("Exponent of Y : "))
exponent = int(input("Exponent of Binomial : "))

polynomial = ""
layer = [1]

for i in range(exponent):
    newLayer = [1]
    for i in range(len(layer) - 1):
        x = True
        newLayer.append(layer[i] + layer[i+1])
    newLayer.append(1)
    layer = newLayer

def formatCoefficient(__coefficient, _firstTerm):
    out = ""
    if _coefficient != 1 and _coefficient != 0:
        if _coefficient != -1:
            if _coefficient > 0 and _firstTerm != True:
                out += "+"
            out += str(__coefficient)
        else:
            out += "-"
    return out

exponent1 = exponent
firstTerm = True
for coefficient in layer:
    term = ""
    exponent2 = exponent - exponent1
    
    _exponentX = exponentX * exponent1
    _exponentY = exponentY * exponent2
    _coefficient = coefficient * (coefficientX ** exponent1) * (coefficientY ** exponent2)

    term += formatCoefficient(_coefficient, firstTerm)
        
    if _exponentX != 0:
        term += "(x)^" + str(_exponentX)
    if _exponentY != 0:
        term += "(y)^"+ str(_exponentY)
        
    polynomial += term
    exponent1 -=1
    firstTerm = False

print()    
print(f"({formatCoefficient(coefficientX, True)}x^{exponentX} + {formatCoefficient(coefficientY, False)}y^{exponentY})^{exponent}")
print("=")
print(polynomial)
