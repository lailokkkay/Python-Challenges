for i in range(1, 21):
    out = ""
    x = False
    if i % 3 == 0:
            out += "Fizz"
            x = True
    if i % 5 == 0:
            out += "Buzz"
            x = True
    if x != True:
        out = i
    print(out)


