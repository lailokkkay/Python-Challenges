import string
characters = []
morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---","-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
             "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
for i in range(len(string.ascii_lowercase)):
    characters.append([string.ascii_lowercase[i], string.ascii_uppercase[i]])
for chr in string.digits:
    characters.append([chr, "0"])

def FindMorseCodeIndex(chr):
    i = 0
    for _chr in characters:
        if _chr[0] == chr or _chr[1] == chr:
            return i
        i += 1

def FindTextIndex(code):
    i = 0
    for _code in morseCode:
        if code == _code:
            return i
        i += 1

def TextToMorseCode(text):
    out = ""
    for chr in text:
        if chr == " ":
            out += "/ "
        else:
            out += morseCode[FindMorseCodeIndex(chr)] + " "
    return out[0:-1]

def MorseCodeToText(morseCode):
    out = ""
    code = ""
    for unit in morseCode:
        if unit == "." or unit == "-":
            code += unit
        else:
            if code != "":
                out += characters[FindTextIndex(code)][0]
                code = ""
            if unit == "/":
                out += " "
    if code != "":
      out += characters[FindTextIndex(code)][0]
    return out

print("##MORSE CODE CONVERTER""##")
print("Letters are separated by spaces and words by slashes.")
print()

while True:
    print("FUNCTIONS : ")
    print("0 - Text to Morse Code")
    print("1 - Morse Code to Text")
    choice = int(input("Enter Choice : "))
    if choice == 0:
        string = input("Enter Text : ")
        print(f"Output : {TextToMorseCode(string)}")
    elif choice == 1:
        string = input("Enter Morse Code : ")
        print(f"Output : {MorseCodeToText(string)}")
    print()