string = input()
vowels = ["a","e","i","o","u"]

def make_it_laugh(string):
    out = ""
    index = 0
    for i in range(0, len(string)):
        isVowel = False
        for vowel in vowels:
            if string[i] == vowel:
                isVowel = True
                out += "haha"
        if isVowel == False:
            out += string[i]
        index += 1
    return out

print(make_it_laugh(string))
