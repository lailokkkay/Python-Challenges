text = input()

wordCount = 0
totalWordLength = 0
newWord = True

for letter in text:
    if letter != " ":
        if newWord:
            wordCount += 1
            newWord = False
        totalWordLength += 1
    else:
        newWord = True

print(totalWordLength / wordCount)

input()
