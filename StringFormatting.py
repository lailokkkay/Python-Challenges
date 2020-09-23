##Exercise 1
ringgit = 125

print(f"RM{ringgit}")

##Exercise 2
headings = ["ones", "twos", "threes"]
ones = [1,2,3]
twos = [2,4,6]
threes = [3,6,9]

spacing = 10

print(f"{headings[0]:^15} {headings[1] :^15} {headings[2]:^15}")
for i in range(0, 3):
    print(f"{ones[i]:^15} {twos[i] :^15} {threes[i]:^15}")

##Exercise 3
print(f"{int(input()):b}")
