import re

with open('input.txt', 'r') as file:
    text = file.readlines()
    text = [line.strip() for line in text]

    aspots = []
    count = 0
    
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] == 'A':
                aspots.append((i, j))

    for spot in aspots:
        if spot[0] == 0 or spot[0] == len(text) - 1 or spot[1] == 0 or spot[1] == len(text[0]) - 1:
            continue
        surrounds = text[spot[0]-1][spot[1]-1] + text[spot[0]-1][spot[1]+1] + text[spot[0]+1][spot[1]-1] + text[spot[0]+1][spot[1]+1]
        if surrounds == 'MMSS' or surrounds == 'SSMM' or surrounds == "MSMS" or surrounds == "SMSM":
            count += 1
    
    print(count)