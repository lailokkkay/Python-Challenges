numbers = [1, 5, 7, 10, 12]

def Difference(num1, num2):
    return abs(num1 - num2)

smallestDifference = Difference(numbers[0], numbers[1])

for i in range(1, len(numbers)):
    currentDifference = Difference(numbers[i], numbers[i - 1])
    if currentDifference < smallestDifference:
        smallestDifference = currentDifference

print(smallestDifference)
    
