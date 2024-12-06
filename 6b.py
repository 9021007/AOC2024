from tqdm import tqdm
from copy import copy, deepcopy

with open('input.txt', 'r') as file:
    orig = file.readlines()
    text = [list(x.strip()) for x in orig]

    start = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == '^' or text[i][j] == 'v' or text[i][j] == '<' or text[i][j] == '>':
                start = [i, j, text[i][j]]

    # print(start)
    # input("start")


    inMap = True
    while inMap:
        curr = []
        for i in range(len(text)):
            for j in range(len(text[i])):
                if text[i][j] == '^' or text[i][j] == 'v' or text[i][j] == '<' or text[i][j] == '>':
                    # print(i, j)
                    curr = [i, j]
                    if text[i][j] == '^' and i == 0:
                        inMap = False
                        text[i][j] = 'P'
                        break
                    elif text[i][j] == 'v' and i == len(text) - 1:
                        inMap = False
                        text[i][j] = 'P'
                        break
                    elif text[i][j] == '<' and j == 0:
                        inMap = False
                        text[i][j] = 'P'
                        break
                    elif text[i][j] == '>' and j == len(text[i]) - 1:
                        inMap = False
                        text[i][j] = 'P'
                        break
                    elif text[i][j] == '^' and text[i-1][j] == "#":
                        text[i][j] = '>'
                    elif text[i][j] == 'v' and text[i+1][j] == "#":
                        text[i][j] = '<'
                    elif text[i][j] == '<' and text[i][j-1] == "#":
                        text[i][j] = '^'
                    elif text[i][j] == '>' and text[i][j+1] == "#":
                        text[i][j] = 'v'
                    elif text[i][j] == '^':
                        text[i][j] = 'P'
                        text[i-1][j] = '^'
                    elif text[i][j] == '>':
                        text[i][j] = 'P'
                        text[i][j+1] = '>'
                    elif text[i][j] == 'v':
                        text[i][j] = 'P'
                        text[i+1][j] = 'v'
                    elif text[i][j] == '<':
                        text[i][j] = 'P'
                        text[i][j-1] = '<'
                    else:
                        print("oops")
                        exit()
    # withpath = text
    withpath = deepcopy(text)
    withpath[start[0]][start[1]] = start[2]
    text = deepcopy(withpath)

    height = len(text)
    width = len(text[0])

    loops = 0
    for a in tqdm(range(height)):
        for b in range(width):
            # print(a, b)
            if text[a][b] == "P":
                text[a][b] = "#"
                looping = False
                inMap = True
                steps = []
                curr = [start[0], start[1]]
                while inMap:
                    i = curr[0]
                    j = curr[1]
                    steps.append([i,j,text[i][j]])
                    # print(steps)
                    if text[i][j] == '^' and i == 0:
                        inMap = False
                        text[i][j] = 'X'
                        steps = []
                        break
                    elif text[i][j] == 'v' and i == len(text) - 1:
                        inMap = False
                        text[i][j] = 'X'
                        steps = []
                        break
                    elif text[i][j] == '<' and j == 0:
                        inMap = False
                        text[i][j] = 'X'
                        steps = []
                        break
                    elif text[i][j] == '>' and j == len(text[i]) - 1:
                        inMap = False
                        text[i][j] = 'X'
                        steps = []
                        break
                    elif text[i][j] == '^' and text[i-1][j] == "#":
                        text[i][j] = '>'
                    elif text[i][j] == 'v' and text[i+1][j] == "#":
                        text[i][j] = '<'
                    elif text[i][j] == '<' and text[i][j-1] == "#":
                        text[i][j] = '^'
                    elif text[i][j] == '>' and text[i][j+1] == "#":
                        text[i][j] = 'v'
                    elif text[i][j] == '^':
                        text[i][j] = 'X'
                        text[i-1][j] = '^'
                        curr = [i-1, j]
                    elif text[i][j] == '>':
                        text[i][j] = 'X'
                        text[i][j+1] = '>'
                        curr = [i, j+1]
                    elif text[i][j] == 'v':
                        text[i][j] = 'X'
                        text[i+1][j] = 'v'
                        curr = [i+1, j]
                    elif text[i][j] == '<':
                        text[i][j] = 'X'
                        text[i][j-1] = '<'
                        curr = [i, j-1]
                    else:
                        print("oops")
                        exit()
                    if [i, j, text[i][j]] in steps:
                        # print("looping")
                        looping = True
                        inMap = False
                        steps = []
                        break
                if looping:
                    loops += 1
                text = []
                text = deepcopy(withpath)

    print("")
    print("")
    print(loops)
    