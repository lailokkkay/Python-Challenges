import string
import random

password = ""

trailingCharacters = 10
drivers = [input("Favourite Colour : "), input("Favourite Place : "), input("Favourite Animal : ")]

for x in drivers:
    for i in x:
        if random.randint(0,1) == 0:
            password += i.upper()
        else:
            password += i.lower()

password += ''.join(random.choice(string.punctuation) for _ in range(trailingCharacters))

print(password)