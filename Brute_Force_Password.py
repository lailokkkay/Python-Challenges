##Function that finds all possible combinations in any base was made seperately so it fits together wierdly :P

import string
import random

characters = string.ascii_letters + string.digits + string.punctuation
passwordLength = 4
password = ""


def GeneratePassword(length):
    _password = ""
    for i in range(length):
        _password += characters[random.randint(0, len(characters) - 1)]
    return _password

def TryPassword(actualPassword, passwordAttempt):
    if passwordAttempt == actualPassword:
        print(f"Found Password = {passwordAttempt}")
        return True

password = GeneratePassword(passwordLength)

print(f"Actualy Password : {password}")
print()

sequence = [[]]
base = len(characters)

def SequenceToPassword(_sequence):
    password = ""
    for i in _sequence:
        password += characters[i]

    return password

def DuplicateArray(_sequence, _base):
    newSequence = []
    for duplicate in range(base):
        for count in range(len(_sequence)):
            k = []
            for copy in _sequence[count]:
                k.append(copy)      
            k.insert(0, duplicate)
            newSequence.append(k)
    return newSequence

r = False

while r != True:
    sequence = DuplicateArray(sequence, base)
    for i in sequence:
        if TryPassword(password, SequenceToPassword(i)):
            r = True
