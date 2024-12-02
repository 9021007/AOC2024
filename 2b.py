from copy import copy

with open('input.txt', 'r') as file:
    text = file.readlines()
    diffs = []
    lines = []
    safe = 0
    fixed = 0

    for i in range(len(text)):
        text[i] = text[i].strip()
        splittext = text[i].split(" ")
        lines.append(splittext)
        thesediffs = []
        for i in range(len(splittext)):
            splittext[i] = int(splittext[i])
        for j in range(len(splittext) - 1):
            # print(splittext[j] - splittext[j+1])
            thesediffs.append(splittext[j] - splittext[j+1])
        diffs.append(thesediffs)


    def checkDiffs(thesediffs):
        thissafe = True
        if thesediffs[0] == 0:
            thissafe = False
        if thesediffs[0] >= 0:
            for j in range(len(thesediffs)):
                if thesediffs[j] > 0 and thesediffs[j] < 4:
                    pass
                else:
                    thissafe = False
        if thesediffs[0] < 0:
            for j in range(len(thesediffs)):
                if thesediffs[j] < 0 and thesediffs[j] > -4:
                    pass
                else:
                    thissafe = False
        return thissafe

    for i in range(len(lines)):
        if checkDiffs(diffs[i]):
            safe += 1
        else:
            for j in range(len(lines[i])):
                temp = copy(lines[i])
                print(temp)
                temp.pop(j)
                tempdiffs = []
                for k in range(len(temp) - 1):
                    tempdiffs.append(temp[k] - temp[k+1])
                if checkDiffs(tempdiffs):
                    safe += 1
                    fixed += 1
                    break
    print(safe)
    print(fixed)
                
