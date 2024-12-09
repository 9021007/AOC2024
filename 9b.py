from tqdm import tqdm

with open('input.txt', 'r') as file:
    text = file.read().strip()
    # print(text)
    fs = []
    for i in range(len(text)):
        if i % 2 == 0:
            # print(text[i], i)
            # file
            for j in range(int(text[i])):
                fs.append(str(int(i/2)))
        else:
            # free
            for i in range(int(text[i])):
                fs.append('.')
    # print(fs)
    skipcount = 0
    initial = ''.join(fs)
    
    for i in tqdm(range(len(fs))):
        if skipcount > 0:
            skipcount = skipcount - 1
            # print("skipping")
            continue
        backi = (len(fs)-1)-i
        if fs[backi] != '.':
            # print(''.join(fs))
            # print(fs)
            foundGroup = False
            tail = backi
            while not foundGroup:
                if fs[tail] == fs[backi]:
                    tail = tail - 1
                else:
                    tail = tail + 1
                    foundGroup = True
            thislen = backi - tail + 1
            # print(tail, backi, fs[tail], fs[backi], thislen)
            gapindex = -1
            candgap = 0
            for j in range(len(fs)):
                if fs[j] != '.':
                    candgap = 0
                else:
                    candgap = candgap + 1
                if candgap == thislen:
                    gapindex = j - thislen + 1
                    break
                

            # print(gapindex)
            if gapindex != -1 and gapindex < tail:
                # print(''.join(fs))
                # print(fs)
                for j in range(thislen):
                    # print(j, "moving", backi+j, " (", fs[backi-j],") to", gapindex+j)
                    fs[gapindex+j] = fs[backi-j]
                    fs[backi-j] = '.'
            else:
                skipcount = thislen - 1
                # print("skipping", skipcount)
    # print(''.join(fs))
    # print(fs)
            
    sum = 0

    for i in range(len(fs)):
        if fs[i] != ".":
            sum += int(fs[i]) * i

    print(sum)