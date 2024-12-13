from copy import deepcopy
import math
from tqdm import tqdm


with open('input.txt', 'r') as file:

    precomploops = 35
    precompnums = 100
    
    precomp = []
    for x in tqdm(range(precom)):
        precomp.append([])
        text = [x]
        for y in range(precomploops):
            newtext = []
            for i in range(len(text)):
                if text[i] == 0:
                    newtext.append(1)
                elif (int(math.log10(text[i]))+1) % 2 == 0:
                    digits = int((int(math.log10(text[i]))+1)/2)
                    newtext.append(int(text[i]/(10**digits)))
                    newtext.append(text[i]-(int(text[i]/(10**digits))*(10**digits)))
                else:
                    newtext.append(text[i] * 2024)
            text = deepcopy(newtext)
            precomp[x].append(len(text))

    sum = 0
    loops = 75

    filetext = file.read().strip().split(" ")
    filetext = [int(x) for x in filetext]
    text = filetext
    
    for x in tqdm(range(loops)):
        newtext = []
        for i in range(len(text)):
            # print(text[i])
            if text[i] < precompnums and x >= loops-precomploops:
                sum += precomp[text[i]][loops-x-1]
                # text.pop(i)               
            elif text[i] == 0:
                newtext.append(1)
            elif (int(math.log10(text[i]))+1) % 2 == 0:
                digits = int((int(math.log10(text[i]))+1)/2)
                newtext.append(int(text[i]/(10**digits)))
                newtext.append(text[i]-(int(text[i]/(10**digits))*(10**digits)))
            else:
                newtext.append(text[i] * 2024)
        text = deepcopy(newtext)

    print(sum)
    print(len(text))
    print(sum + len(text))