import math
import string

triangleNumbers = 0

def IsTriangle(num):
    out = 0
    if (math.sqrt(2 * num + 1/4) - 1/2).is_integer():
        out = 1
    return out

def WordValue(word):
    value = 0
    for char in word:
        value += 1 + string.ascii_uppercase.find(char)
    return value

currentWord = ""

with open("words.txt", "r") as file:
    for line in file:
        for char in line:
            if char != '"' and char != ',':
                currentWord += char
            elif currentWord != "":
                triangleNumbers += IsTriangle(WordValue(currentWord))
                currentWord = ""

print(triangleNumbers)
