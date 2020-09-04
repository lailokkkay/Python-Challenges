word = input()
vowels = ["a","e","i","o","u"]
out = ""
group = ""
prev = word[0]
index = 0

for letter in word:
    isVowel = False
    for i in vowels:
        if i == letter:
            isVowel = True
    if letter != prev and group != "":
        out += group + "o" + group
        group = ""
    if isVowel == False:
        group += letter
    else:
        out += letter
    index += 1
    if index == len(word):
        out += group + "o" + group
    prev = letter
    
print(out)
