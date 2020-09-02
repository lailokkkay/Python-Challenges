import random
list = []
count = 0
total = 0
maximum = 0
minimum = 100

while count < 50:
    num = random.randint(1,100)
    total += num
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num
    list.append(num)
    count += 1

print(list)
print(minimum)
print(maximum)
print(total/50)
