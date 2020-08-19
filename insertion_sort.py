import random

list = []

for i in range(9):
    list.append(random.randint(1,9))

print(list)

for i in range(1, len(list)):
    target = i
    
    while list[i] < list[target - 1] and target > 0:
        target -= 1
    list.insert(target, list[i])
    list.pop(i + 1)
    
print(list)
