import random
import time
import copy
import math

class Pattern:
    def __init__(self):
        self.falseLetters = set()
        self.unfixedLetters = {}
        self.fixedLetters = {}

    def Union(self, pattern):
        for i in pattern.unfixedLetters:
            self.unfixedLetters[i] = pattern.unfixedLetters[i]
        for i in pattern.fixedLetters:
            self.fixedLetters[i] = pattern.fixedLetters[i]
        self.falseLetters = self.falseLetters.union(pattern.falseLetters)

    def AddFalse(self, letter):
        newPattern = copy.deepcopy(self)
        newPattern.falseLetters.add(letter)
        return newPattern
    
    def AddUnfixed(self, letter, index):
        newPattern = copy.deepcopy(self)
        newPattern.unfixedLetters[index] = letter
        return newPattern

    def AddFixed(self, letter, index):
        newPattern = copy.deepcopy(self)
        newPattern.fixedLetters[index] = letter
        return newPattern
 
def LetterInWord(letter, word):
    for i in word:
        if letter == i:
            return True
    return False

def MatchingWord(word, pattern):
    for i in pattern.fixedLetters:
        if word[i] != pattern.fixedLetters[i]:
            return False
    for i in pattern.unfixedLetters:
        if pattern.unfixedLetters[i] == word[i] or LetterInWord(pattern.unfixedLetters[i], word) == False:
            return False
    for letter in pattern.falseLetters:
        if LetterInWord(letter, word) == True:
            return False
    return True

def NewPossibleWords(pattern, possibleWords):
    newWords = []
    for i in possibleWords:
        if MatchingWord(i, pattern) == True:
            newWords.append(i)
    return newWords
    
def Entropy(word, wordSet):
    probabilityDist = {}
    expectedInformation = 0
    size = len(wordSet)
    for i in wordSet:
        pattern = Match(i, word)
        if pattern in probabilityDist:
            probabilityDist[pattern] += 1
        else:
            probabilityDist[pattern] = 1
    for i in probabilityDist:
        n = probabilityDist[i]
        if n != 0:
            p = n / size
            expectedInformation += p * (-math.log2(p))
    return expectedInformation

def Match(answer, guess):
    out = {}
    _answer = {}
    _guess = {}
    toRemove = []
    for i in range(5):
        _answer[i] = answer[i]
        _guess[i] = guess[i]

    ##green
    for i in _answer:
        if answer[i] == guess[i]:
            out[i] = '0'
            toRemove.append(i)

    for i in toRemove:
        _answer.pop(i)
        _guess.pop(i)
    toRemove.clear()

    ##yellow
    for i in _answer:
        if LetterInDict(_answer[i], _guess):
            out[i] = '1'
            toRemove.append(i)
    for i in toRemove:
        _guess.pop(i)

    ##grey
    for i in _guess:
        out[i] = '2'
    pattern = ""
    for i in range(5):
        pattern += out[i]
    return pattern

def LetterInDict(letter, word):
    for i in word:
        if word[i] == letter:
            return True
    return False

def CheckGuess(guess, word):
    output = ""
    pattern = Pattern()
    for i in range(len(guess)):
        if guess[i] == word[i]:
            pattern.fixedLetters[i] = guess[i]
            output += '🟩'
        elif LetterInWord(guess[i], word):
            pattern.unfixedLetters[i] = guess[i]
            output += '🟨'
        else:
            pattern.falseLetters.add(guess[i])
            output += '⬛'
    print(output)
    return pattern
 
def Wordle():
    length = 2315
    index = random. randint(1,2315)
    answer = ""
    pattern = Pattern()
    answerTable = {}
    possibleWords = []
    with open('answers.txt', 'r') as f:
        for i in range(index - 1):
            f.readline()
        answer = f.readline().strip()
    with open('answers.txt', 'r') as f:
        for line in f:
            word = line.strip()
            possibleWords.append(word)
            answerTable[word] = True
    with open('exc_guesses.txt', 'r') as f:
        for line in f:
            word = line.strip()
            possibleWords.append(word)
            answerTable[word] = False

    total = len(possibleWords)
    guesses = 0

    guess = "tares"
    while len(pattern.fixedLetters) < 5:
        print(f"//round {guesses + 1}")
        print(f"remaining words = {len(possibleWords)}, uncertainty = {round(math.log2(len(possibleWords)),2)} bits")
        if len(possibleWords) < total:  
            max = [0, None]
            realAnswers = []
            if len(possibleWords) < total:
                for word in possibleWords:
                    if len(realAnswers) < 10:
                        if answerTable[word] == True:
                            realAnswers.append(word)
                    e = Entropy(word, possibleWords)
                    if e > max[0]:
                        max[0] = e
                        max[1] = word
                print(f"highest information = {max[1]} {round(max[0], 2)} bits")
                print(f"possible answers = {realAnswers}")
            if len(realAnswers) == 1:
                guess = realAnswers[0]
            else:
                guess = max[1]
        else:
            print(f"highest information = tares 6.34 bits")    
        print(f"guess = {guess}")
        pattern.Union(CheckGuess(guess, answer))
        possibleWords = NewPossibleWords(pattern, possibleWords)
        guesses += 1
        print()
    print(f"score = {guesses}")

def GetPattern(pattern, word):
    newPattern = Pattern()
    for i in range(5):
        if pattern[i] == '0':
            newPattern.fixedLetters[i] = word[i]
        elif pattern[i] == '1':
            newPattern.unfixedLetters[i] = word[i]
        elif pattern[i] == '2':
            newPattern.falseLetters.add(word[i])
    print(vars(newPattern))
    return newPattern   

def ManualWordle():
    pattern = Pattern()
    answerTable = {}
    possibleWords = []
    with open('answers.txt', 'r') as f:
        for line in f:
            word = line.strip()
            possibleWords.append(word)
            answerTable[word] = True
    with open('exc_guesses.txt', 'r') as f:
        for line in f:
            word = line.strip()
            possibleWords.append(word)
            answerTable[word] = False

    total = len(possibleWords)
    guesses = 1

    guess = "tares"
    print(guess)
    pattern.Union(GetPattern(input("pattern : "), guess))
    possibleWords = NewPossibleWords(pattern, possibleWords)
    print(len(possibleWords))

    while len(pattern.fixedLetters) < 5:   
        max = [0, None]
        realAnswers = []

        for word in possibleWords:
            if len(realAnswers) < 5:
                if answerTable[word] == True:
                    realAnswers.append(word)
            e = Entropy(word, possibleWords)
            if e > max[0]:
                max[0] = e
                max[1] = word
        print(max)
        print(realAnswers)

        guess = None
        if len(realAnswers) == 1:
            guess = realAnswers[0]
        else:
            guess = max[1]
        print(guess)
        pattern.Union(GetPattern(input("pattern : "), guess))
        possibleWords = NewPossibleWords(pattern, possibleWords)
        print(len(possibleWords))

Wordle()