def AllStrings(length, string, letterSet):
    if length == 0:
        print(string)
        return
    for i in letterSet:
        AllStrings(length-1, string + i, letterSet)

AllStrings(3, "", ['a', 'b', 'c'])