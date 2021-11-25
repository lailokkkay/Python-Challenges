fSrc = open("practical.txt", 'r')
fNew = open("newPractical.txt", 'a')

dlmtrs = ["19.1", "19.2", "20.1", "20.2"]
currDlmtr = ""
for line in fSrc:
    flg = True
    tag = line[0]+line[1]+line[2]+line[3]
    for s in dlmtrs:
        if s == tag:
            currDlmtr = s+"\t"
            flg = False
    if flg == True:
        fNew.write(currDlmtr + line)
fNew.close()
