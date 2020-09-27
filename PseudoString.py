""" Making Pseudocode real. Create the Pseudocode in Python.
By the way this is NOT a nice way to name your definitions in Python, but it 
lets you get away with it.
pass lets me not code up the function. It's like on a quiz show.
"""

def LEFT(string,length):
    # returns the left most characters of a string. 
    # I've done this one as an example.
    return string[0:length]

def RIGHT(string,length):
    # Returns the right most characters of a string
    return string[-length:]

def MID (string,start,end):
    # Returns string from position x, length y. Note that the count starts at 1. 
    return string[start - 1 : end - 1]
    
def LENGTH (string):
    #Returns the lengths of a string
    return len(string)

def LCASE (char):
# From here on in you need to figure out the parameters and the function.  
    return char.lower()
    
def UCASE(char):
    #Returns the upper case character. (Does nothing if already upper case). Note that this works on characters rather than a string.
    return char.upper()

def TO_UPPER(string):
    #Returns a string in upper class. (Non-alphabetic characters and upper case characters remain unchanged)
    return string.upper()
 
def TO_LOWER(string):
  #Returns a string in lower class. (Non-alphabetic characters and lower case characters remain unchanged)
    return string.lower()
    pass
 
def NUM_TO_STRING(float):
    return str(float)

def STRING_TO_NUM(string):
    return float(string)

def INT(string):
    return int(string)

def ASC(char):
    #Changes a character into its ASCII number.
    return ord(char)

#Extension 2
import random

def GenerateString(case):
    inputs = ["This sucks on ice!"]
    if case == 0:
        inputs[0] = TO_LOWER(inputs[0])
    elif case == 1:
        inputs[0] = TO_UPPER(inputs[0])
    return inputs

def GenerateLength():
    inputs = GenerateString(None)
    inputs.append(random.randint(0, len(inputs[0]) - 1))
    return inputs

def GenerateMid():
    inputs = GenerateString(None)
    end = random.randint(1, len(inputs[0]))
    start = random.randint(1, end - 1)
    inputs.append(start)
    inputs.append(end)
    return inputs

def GenerateChar(case):
    inputs = ["c"]
    if case == 1:
        inputs[0] = UCASE(inputs[0])
    return inputs

def GenerateStringInt():
    inputs = ["543"]
    return inputs

def GenerateFloat():
    inputs = [12.79]
    return inputs

numberOfQuestions = 10
score = 0

functionNameIndex = 0
callFunctionIndex = 1
functionInputsIndex = 2

functions = []
functions.append(["LEFT", "RIGHT", "MID", "LENGTH", "LCASE", "UCASE", "TO_UPPER", "TO_LOWER", "NUM_TO_STRING", "STRING_TO_NUM", "INT", "ASC"])
functions.append([LEFT, RIGHT, MID, LENGTH, LCASE, UCASE, TO_UPPER, TO_LOWER, NUM_TO_STRING, STRING_TO_NUM, INT, ASC])
functions.append([GenerateLength(), GenerateLength(), GenerateMid(), GenerateString(None), GenerateChar(1), GenerateChar(None), GenerateString(0), GenerateString(1), GenerateFloat(), GenerateFloat(), GenerateStringInt(), GenerateChar(None)])

def GenerateQuestion():
    functionIndex = random.randint(0, len(functions[functionNameIndex]) - 1)
    inputs = functions[functionInputsIndex][functionIndex]
    stringInputs = ""
    for i in inputs:
        stringInputs += f"{i}, "
    stringInputs = stringInputs[0:-2]

    print(f"x <- {functions[functionNameIndex][functionIndex]}({stringInputs})")
    answer = None
    if len(inputs) == 1:
        answer = functions[callFunctionIndex][functionIndex](inputs[0])
    elif len(inputs) == 2:
        answer = functions[callFunctionIndex][functionIndex](inputs[0], inputs[1])
    elif len(inputs) == 3:
        answer = functions[callFunctionIndex][functionIndex](inputs[0], inputs[1], inputs[2])

    print(answer)

    if type(answer)(input("x : ")) == answer:
        return True

for i in range(1 , numberOfQuestions + 1):
    print(f"Question {i}")
    if GenerateQuestion():
        score += 1
    print()

print(f"score = {Score} / {numberOfQuestions}")