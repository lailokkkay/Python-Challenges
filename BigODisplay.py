import matplotlib.pyplot as plt
import math

def RealPlot(func, colour):
    x = []
    y = []
    funcs = [Quadratic, Exponential, Logarithmic]
    upper = 5
    numPoints = 20
    spacing = upper / numPoints
    for i in range(1,numPoints + 1):
        var = i*spacing
        x.append(var)
        y.append(funcs[int(func)](var))
        plt.plot(x ,y, colour,linewidth=1.0)

def IntPlot(func,colour):
    x = []
    y = []
    funcs = [Factorial]
    upper = 5
    for i in range(upper + 1):
        x.append(i)
        y.append(funcs[int(func)](i))
        plt.plot(x ,y, colour ,linewidth=1.0)

def Quadratic(_var):
    return _var**2
def Exponential(_var):
    return 2 ** _var
def Logarithmic(_var):
    return math.log(_var, 2)
def Factorial(_var):
    out = 1
    for i in range(1,int(_var+1)):
        out *= i
    return out

RealPlot(0, "b")
RealPlot(1, "g")
RealPlot(2, "y")
IntPlot(0, "r")

plt.show()