def RemoveDuplicates(_list):
    seenItems = []
    for item in _list:
        index = 0
        itemFound = False
        size = len(seenItems)
        if size != 0:
            while itemFound == False and index <= size-1:
                if item == seenItems[index]:
                    itemFound = True
                else:
                    index += 1
        if itemFound == False:
            seenItems.append(item)
    return seenItems
