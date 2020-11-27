ifCounter1 = 0
ifCounter2 = 0
out = ""

def FindIf(_line):
    total = 0
    section = "__"
    for char in _line:
        section = section[1] + char
        if section == "If":
            total += 1
    return total

with open("if.txt","r") as whole_file:
   for line in whole_file:
        ifCounter1 += FindIf(line)

with open("mam.txt","r") as whole_file:
   for line in whole_file:
        ifCounter2 += FindIf(line)

if ifCounter1 == ifCounter2:
    out = "Neither has more."
elif ifCounter1 > ifCounter2:
    out = "if.txt has more."
else:
    out = "mam.txt has more."
    
with open("if.txt","a") as existing_file:
    existing_file.write("\n" + f"If count = {ifCounter1}, {out}")
    
with open("mam.txt","a") as existing_file:
    existing_file.write("\n" + f"If count = {ifCounter2}, {out}")
