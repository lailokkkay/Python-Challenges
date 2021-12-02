import os

fN = input("file name : ")

try:
    open(fN,"r")
except FileNotFoundError:
    print(os.getcwd())
    for f in os.listdir('.'):
        print(f)
