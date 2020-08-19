piramidSize = int(input())
currentLayer = "x"

for i in range(piramidSize):
    print(currentLayer)
    currentLayer += "xx"
