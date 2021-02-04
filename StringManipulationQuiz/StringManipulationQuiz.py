##References
import string
import random


##String Manipulation Functions
def RandomString(length):
    out = ""
    for i in range(length):
        out += string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase)-1)]
    return out

def LEFT():
    word = RandomString(random.randint(3,15))
    reach = random.randint(1, len(word))
    return (f'LEFT("{word}", {reach})', word[:reach])

def RIGHT():
    word = RandomString(random.randint(3,15))
    reach = random.randint(1, len(word))
    return (f'RIGHT("{word}", {reach})', word[len(word)-reach::])

def MID():
    word = RandomString(random.randint(3,15))
    reach = [random.randint(1, len(word) - 1)]
    reach.append(random.randint(reach[0] + 1, len(word)))
    return (f'MID("{word}", {reach[0]}, {reach[1]})', word[reach[0]:reach[1]])

stringFunctions = [LEFT,RIGHT,MID]

##Question Processing
def QuestionCaller(questionNumber):
    passed = False
    qData = stringFunctions[random.randint(0,len(stringFunctions) - 1)]()
    print(f"{questionNumber}. x <- {qData[0]}")
    if qData[1] == input("          x = "):
        passed = True
    else:
        print("Wrong Answer!")
    return passed

def Main(): 
    print("##STRING MANIPULATION TEST##")
    print("Give the value of the variables for the following sequence of statements.")
    print()

    score = 0
    count = 1

    while QuestionCaller(count) != False:
        print()
        count += 1
        score += 1

    WriteHighScore(score)
    print(f"Final Score = {score}")

##File Handling
def WriteHighScore(newScore): ##If a score is in the top (10) of all time, the score is added to the appropriate place and the last score is removed. 
    newScores = []
    placeFound = False
    
    with open("Highscores.txt", "r") as currentScores:
        for score in currentScores:
            curr = int(score[score.find(" ")::])
            if curr >= newScore or placeFound == True:
                newScores.append(curr)
            else:
                placeFound = True
                newScores.append(newScore)
                newScores.append(curr)
        if placeFound == True:
            newScores.pop(-1)

    with open("Highscores.txt", "w") as newSave:
        count = 0
        for score in newScores:
            count += 1
            newSave.write(f"{count}) {score}\n")
            
def ClearHighScores():  ##Clear leaderboard and define places.    
    with open("Highscores.txt", "w") as clearSave:
        places = 10
        count = 0
        for i in range(places):
            count += 1
            clearSave.write(f"{count}) 0\n")

##Start Questioning
Main()
