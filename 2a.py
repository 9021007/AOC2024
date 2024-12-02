with open('input.txt', 'r') as file:
    text = file.readlines()
    safe = 0
    diffs = []

    for i in range(len(text)):
        text[i] = text[i].strip()
        splittext = text[i].split(" ")
        thesediffs = []
        for i in range(len(splittext)):
            splittext[i] = int(splittext[i])
        for j in range(len(splittext) - 1):
            # print(splittext[j] - splittext[j+1])
            thesediffs.append(splittext[j] - splittext[j+1])
        diffs.append(thesediffs)

    for i in range(len(diffs)):
        thissafe = True
        if diffs[i][0] == 0:
            thissafe = False
        if diffs[i][0] >= 0:
            for j in range(len(diffs[i])):
                if diffs[i][j] > 0 and diffs[i][j] < 4:
                    pass
                else:
                    thissafe = False
        if diffs[i][0] < 0:
            for j in range(len(diffs[i])):
                if diffs[i][j] < 0 and diffs[i][j] > -4:
                    pass
                else:
                    thissafe = False
        if thissafe:
            safe += 1
    
    print(safe)