ISBN10 = str(input())

total = 0
index = 10
count = 0

for i in range(0,10):
    total += int(ISBN10[i]) * index
    index -= 1

if total % 11 == 0:
    print("Check digit is valid.")
else:
    print("Check digit is invalid.")
