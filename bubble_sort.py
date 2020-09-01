import random

list = []

for i in range(9):
    list.append(random.randint(1,9))

print(list)

swapped = True

while swapped:
    swapped = False
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            list.insert(i + 2, list[i])
            list.pop(i)
            swapped = True

print(list)