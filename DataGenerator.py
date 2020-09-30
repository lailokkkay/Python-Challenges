import random
import datetime

def GenerateINTEGER():
    return random.randint(-100, 100)

def GenerateREAL():
    return random.randint(-10000, 10000) / 100

def GenerateCHAR():
    return "c"

def GenerateSTRING():
    return "ouing))E)F)3r2]23]23[d\==1-easODJAS"

def GenerateBOOLEAN():
    out = None
    if random.randint(0,1) == 1:
        out = True
    else:
        out = False
    return out

def GenerateDATE():
    return datetime.datetime(random.randint(0, 2020), random.randint(1, 12), random.randint(1, 30))

print(GenerateREAL())
