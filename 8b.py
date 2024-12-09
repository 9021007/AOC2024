from copy import deepcopy

with open('input.txt', 'r') as file:
    text = file.readlines()
    text = ([list(x.strip()) for x in text])
    orig = deepcopy(text)
    # print(orig)
    freqs = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] != '.' and freqs.count(text[i][j]) == 0:
                freqs.append(text[i][j])
    map = {}
    for i in range(len(freqs)):
        map[freqs[i]] = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] != '.':
                map[text[i][j]].append((i, j))
    print(map)
    for i in range(len(map)):
        for j in range(len(map[freqs[i]])):
            for k in range(len(map[freqs[i]])):
                if j != k:
                    for l in range(len(orig)):
                        xdiff = map[freqs[i]][j][0] - map[freqs[i]][k][0]
                        ydiff = map[freqs[i]][j][1] - map[freqs[i]][k][1]
                        xdiff = xdiff * l
                        ydiff = ydiff * l
                        newx = map[freqs[i]][j][0] + xdiff
                        newy = map[freqs[i]][j][1] + ydiff
                        try:
                            if newx >= 0 and newy >= 0:
                                text[newx][newy] = "#"
                        except:
                            pass

    sum = 0

    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == "#":
                sum += 1

    for i in range(len(text)):
        print("".join(text[i]))
    
    print(sum)