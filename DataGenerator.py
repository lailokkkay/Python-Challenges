import random
import string
import datetime

def GenerateINTEGER():
    return random.randint(-100, 100)

def GenerateREAL():
    return random.randint(-10000, 10000) / 100

def GenerateCHAR():
    return ''.join(random.choice(string.ascii_letters))

def GenerateSTRING():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def GenerateBOOLEAN():
    out = None
    if random.randint(0,1) == 1:
        out = True
    else:
        out = False
    return out

def GenerateDATE():
    return datetime.datetime(random.randint(0, 2020), random.randint(1, 12), random.randint(1, 30))

lives = 3
points = 0
bonusThreshold = 5
rewardPoints = 10
bonusPoints = 5
count = 1
functions = [GenerateINTEGER, GenerateREAL, GenerateCHAR, GenerateSTRING, GenerateBOOLEAN, GenerateDATE]
answers = ["INTEGER", "REAL", "CHAR", "STRING", "BOOLEAN", "DATE"]

while lives > 0:
    print("Question", count)
    print("Score =", points)
    count += 1
    index = random.randint(0, len(functions) - 1)
    print(functions[index]())
    firstTime = datetime.datetime.now()
    if input("Data Type : ") == answers[index]:
        points += rewardPoints
        if (datetime.datetime.now() - firstTime).total_seconds() < bonusThreshold:
            points += bonusPoints
        print("Correct!")
        
    else:
        lives -= 1
        print("Wrong!")
    print()

print("Game Over!")
print("Score =", points)
