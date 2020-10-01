array = [234,23423,214,1234,2134]
search = int(input())

index = 0
itemFound = False
for i in array:
    if i == search:
        itemFound = True
        print(f"Index of item in array is {index}.")
    index += 1
    
if itemFound == False:
    print("Item is not in array.")
