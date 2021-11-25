import pickle

class DataObj:
    def __init__(self, chapter, point):
        self.chapter = chapter
        self.point = point
        self.read = False

objList = []

def ReadFile():
    with open("newPractical.txt", 'r') as fSrc:
        for line in fSrc:
            objList.append(DataObj(line[:4], line[5::]))

def ClearPickle():
    with open("database.pickle", "wb") as fPck:
        pickle.dump(None, fPck)

def SavePickle():
    with open("database.pickle", "wb") as fPck:
        pickle.dump(objList, fPck)

def LoadPickle():
    with open("database.pickle", "rb") as fPck:
        return pickle.load(fPck)

def PrintList():
    print()
    print("index|chapter|read")
    num = 0
    for i in objList:
        print(num,i.chapter, i.read)
        num+=1

def Query(_chapter):
    out = []
    for i in objList:
        if i.chapter == _chapter:
            out.append(i)
    return out

def InsertEntry(chapter, point):
    objList.append(DataObj(chapter,point))

while True:
    cmd = input("0=load;1=print;2=query;save=3;reset=4")
    if cmd == '0':
        objList = LoadPickle()
    elif cmd == '1':
        PrintList()
    elif cmd == '2':
        select = []
        cmd1 = input("0=index,1=chapter")
        if cmd1 == '0':
            select.append(objList[int(input("index="))])
        if cmd1 == '1':
            select = Query(input("chapter="))

        status = bool(input("True/False"))
        for i in select:
            i.read = status
    elif cmd == '3':
        SavePickle()
    elif cmd == '4':
        ReadFile()






        
