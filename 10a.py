with open('input.txt', 'r') as file:
    text = file.readlines()
    text = [list(x.strip()) for x in text]
    heads = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            text[i][j] = int(text[i][j])
            if text[i][j] == 0:
                heads.append((i, j))
    
    print(text)
    print(heads)

    sum = 0

    total = [[0,[]] for i in range(len(heads))]

    def recurPathCheck(x,y,i):
        current = text[x][y]
        print(x, y, current)  
        foundany = False 
        if current == 9:
            print("found ", i)
            global total
            global sum
            if [x,y] not in total[i][1]:
                total[i][1].append([x,y])
                total[i][0] = total[i][0] + 1
                sum += 1
            return
        if x > 0:
            if text[x-1][y] == current + 1:
                foundany = True
                recurPathCheck(x-1, y, i)
        if x < len(text)-1:
            if text[x+1][y] == current + 1:
                foundany = True
                recurPathCheck(x+1, y, i)
        if y > 0:
            if text[x][y-1] == current + 1:
                foundany = True
                recurPathCheck(x, y-1, i)
        if y < len(text[x])-1:
            if text[x][y+1] == current + 1:
                foundany = True
                recurPathCheck(x, y+1, i)
        if not foundany:
            print("dead end")
        

    for i in range(len(heads)):
        recurPathCheck(heads[i][0], heads[i][1], i)

    print(total)
    print(sum)
