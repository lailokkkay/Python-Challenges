string = "This sucks on ice!"

def ReverseString(_string):
    return string[-1 : -len(string) - 1 : -1]

print(ReverseString(string))
