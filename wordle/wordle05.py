import random
import math
import time
import json

class Pattern:
    def __init__(self):
        self.falseLetters = set()
        self.unfixedLetters = {}
        self.fixedLetters = {}

def StringToDict(word):
    out = {}
    for i in range(5):
        out[i] = word[i]
    return out

def DictToString(word):
    out = ""
    for i in range(5):
        out += word[i]
    return out

def LetterInWord(letter, word):
    for i in word:
        if letter == i:
            return True
    return False

def LetterInWordIndex(letter, word):
    for i in word:
        if word[i] == letter:
            return i
    return False

def LetterInDict(letter, word):
    for i in word:
        if word[i] == letter:
            return True
    return False

def MatchingWord(word, pattern):
    fixedLetters = pattern.fixedLetters.copy()
    unfixedLetters = pattern.unfixedLetters.copy()
    falseLetters = pattern.falseLetters.copy()
    word = StringToDict(word)
    keys = []
    ##green
    for i in fixedLetters:
        keys.append(i)
    for i in keys:
        if word[i] != fixedLetters[i]:
            return False
        word.pop(i)
        fixedLetters.pop(i)
    keys.clear()
    ##yellow
    for i in unfixedLetters:
        keys.append(i)
    for i in keys:
        if word[i] == unfixedLetters[i] or LetterInDict(unfixedLetters[i], word) == False:
            return False
        word.pop(i)
        unfixedLetters.pop(i)
    ##grey
    for letter in falseLetters:
        if LetterInDict(letter, word) == True:
            return False
    return True

def NewPossibleWords(pattern, possibleWords):
    newWords = []
    for i in possibleWords:
        if MatchingWord(i, pattern) == True:
            newWords.append(i)
    return newWords
    
def Entropy(word, wordSet, wordMatches):
    probabilityDist = {}
    expectedInformation = 0
    size = len(wordSet)
    for i in wordSet:
        pattern = wordMatches[i]
        if pattern in probabilityDist:
            probabilityDist[pattern] += 1
        else:
            probabilityDist[pattern] = 1
    for i in probabilityDist:
        n = probabilityDist[i]
        if n != 0:
            p = n / size
            expectedInformation += p * -math.log2(p)
    return expectedInformation

def Match(guess, answer):
    out = {}
    answer = StringToDict(answer)
    guess = StringToDict(guess)
    keys = []
    ##green
    for i in guess:
        keys.append(i)
    for i in keys:
        if answer[i] == guess[i]:
            out[i] = '0'
            answer.pop(i)
            guess.pop(i)
    keys.clear()
    ##yellow
    for i in guess:
        keys.append(i)
    for i in keys:
        if LetterInDict(guess[i], answer):
            out[i] = '1'
            guess.pop(i)
            answer.pop(i)
    ##grey
    for i in guess:
        out[i] = '2'
    return DictToString(out)

def CheckGuess(guess, answer):
    pattern = Pattern()
    out = {}
    answer = StringToDict(answer)
    guess = StringToDict(guess)
    keys = []
    ##green
    for i in guess:
        keys.append(i)
    for i in keys:
        if answer[i] == guess[i]:
            out[i] = '🟩'
            pattern.fixedLetters[i] = answer[i]
            answer.pop(i)
            guess.pop(i)
    keys.clear()
    ##yellow
    for i in guess:
        keys.append(i)
    for i in keys:
        if LetterInDict(guess[i], answer):
            out[i] = '🟨'
            pattern.unfixedLetters[i] = guess[i]
            guess.pop(i)
            answer.pop(i)
    ##grey
    for i in guess:
        out[i] = '⬛'
        pattern.falseLetters.add(guess[i])
    print(DictToString(out))
    return pattern

def GetPattern(pattern, word):
    newPattern = Pattern()
    for i in range(5):
        if pattern[i] == '0':
            newPattern.fixedLetters[i] = word[i]
        elif pattern[i] == '1':
            newPattern.unfixedLetters[i] = word[i]
        elif pattern[i] == '2':
            newPattern.falseLetters.add(word[i])
    return newPattern   

def Wordle(matchTable, isOnline):
    pattern = Pattern()
    answerTable = {}
    allGuesses = []
    possibleWords = []
    realAnswers = []
    print("loading words...")
    with open('answers.txt', 'r') as f:
        for line in f:
            word = line.strip()
            realAnswers.append(word)
            possibleWords.append(word)
            answerTable[word] = True
    with open('exc_guesses.txt', 'r') as f:
        for line in f:
            word = line.strip()
            possibleWords.append(word)
            answerTable[word] = False
    print()

    if isOnline == False:
        answer = realAnswers[random.randint(0,len(realAnswers)-1)]
    allGuesses = possibleWords.copy()

    total = len(possibleWords)
    guesses = 0
    guess = ""
    firstGuess = 'soare'
    max = [Entropy(firstGuess, realAnswers, matchTable[firstGuess]), firstGuess]
    while len(pattern.fixedLetters) < 5:
        print(f"//round {guesses + 1}")
        print(f"remaining words = {len(possibleWords)}, uncertainty = {round(math.log2(len(possibleWords)),2)} bits")

        if guesses > 0:
            max = [0, None]   
            for word in allGuesses:
                e = Entropy(word, realAnswers, matchTable[word])
                if e > max[0]:
                    max[0] = e
                    max[1] = word
        print(f"highest information = {max[1]} {round(max[0], 2)} bits")
        print(f"possible answers = {len(realAnswers)}, {realAnswers[0:10]}")
        if len(realAnswers) <= 2:
            guess = realAnswers[0]
        else:
            guess = max[1]

        print(f"guess = {guess}")
        if isOnline == False:
            pattern = CheckGuess(guess, answer)
        else:
           pattern = GetPattern(input("pattern : "), guess)
        possibleWords = NewPossibleWords(pattern, possibleWords)
        realAnswers = []
        for word in possibleWords:
            if answerTable[word] == True:
                realAnswers.append(word)
        guesses += 1
        print()
    print(f"score = {guesses}")
    print()

def WriteMatchTable():
    matchTable = {}
    possibleWords = []
    realAnswers = []
    with open('answers.txt', 'r') as f:
        for line in f:
            word = line.strip()
            realAnswers.append(word)
            possibleWords.append(word)
    with open('exc_guesses.txt', 'r') as f:
        for line in f:
            word = line.strip()
            possibleWords.append(word)
    for i in possibleWords:
        matchTable[i] = {}
        for j in realAnswers:
            matchTable[i][j] = Match(i,j)
    with open("match_table.json", 'w') as f:
        f.write(json.dumps(matchTable))

def LoadMatchTable():
    print("loading match table...")
    with open("match_table.json", 'r') as f:
        matchTable = json.loads(f.read())
    return matchTable

matchTable = LoadMatchTable()

while True:
    c = input('0 = local, 1 = online, 2 = break : ')
    if c == '2':
        break
    elif c == '0':
        Wordle(matchTable, False)
    elif c == '1':
        Wordle(matchTable, True)
