candidates = ["Alice", "Bob", "Charlie"]
votes = [[0,1,2], [0,2,1], [1,2,0], [1,0,2], [2,0,1]]

def CountVotes():
    count = [0 * n for n in range(len(candidates))]      
    for i in votes:
        count[i[0]] += 1
    return count

def EliminateSmallest():
    count = CountVotes()
    minimum = [0]
    for i in range(len(candidates)):
        if count[i] < count[minimum[0]]:
            minimum = [i]
        elif count[i] == count[minimum[0]] and minimum[0] != i:
            minimum.append(i)
    x = 0
    for i in minimum:
        candidates.pop(minimum[-(x+1)])
        for c in votes:
            c.remove(i)
        x += 1

def MajorityVote():
    out = None
    count = CountVotes()
    maximum = 0
    for i in range(len(candidates)):
        if count[i] > count[maximum]:
            maximum = [i]
    if count[maximum] > len(votes)/2:
        out = candidates[maximum]
    else:
        out = False
    return out

while MajorityVote() == False:
    EliminateSmallest()
    
print(MajorityVote())
