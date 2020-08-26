neatnumbers = []

for i in range(101, 1001):
    places = 1
    total = i % pow(10, places)
    digitsum = total

    while i / pow(10, (places)) >= 1:
        places += 1
        digitsum += (i % pow(10, places) - total) / pow(10, places - 1)
        total += i % pow(10, places) - total

    if i % digitsum == 0:
        neatnumbers.append(i)
        count += 1

print(neatnumbers)