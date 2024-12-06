with open('input.txt', 'r') as file:
    text = file.readlines()
    text = [list(x.strip()) for x in text]
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
                        text[i][j] = 'X'
                        break
                    elif text[i][j] == 'v' and i == len(text) - 1:
                        inMap = False
                        text[i][j] = 'X'
                        break
                    elif text[i][j] == '<' and j == 0:
                        inMap = False
                        text[i][j] = 'X'
                        break
                    elif text[i][j] == '>' and j == len(text[i]) - 1:
                        inMap = False
                        text[i][j] = 'X'
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
                    elif text[i][j] == '>':
                        text[i][j] = 'X'
                        text[i][j+1] = '>'
                    elif text[i][j] == 'v':
                        text[i][j] = 'X'
                        text[i+1][j] = 'v'
                    elif text[i][j] == '<':
                        text[i][j] = 'X'
                        text[i][j-1] = '<'
                    else:
                        print("oops")
                        exit()
        # print(curr)
    sum = 0
    for line in text:
        print(''.join(line))
        sum += line.count('X')
    
    print(sum)