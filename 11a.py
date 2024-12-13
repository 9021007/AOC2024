from copy import deepcopy

with open('input.txt', 'r') as file:
    text = file.read().strip().split(" ")
    for x in range(30):
        newtext = []
        for i in range(len(text)):
            if str(int(text[i])) == "0":
                newtext.append("1")
            elif len(str(int(text[i]))) % 2 == 0:
                newtext.append(str(int(text[i]))[:len(str(int(text[i])))//2])
                newtext.append(str(int(text[i]))[len(str(int(text[i])))//2:])
            else:
                newtext.append(str(int(text[i]) * 2024))
        text = deepcopy(newtext)
        # print(text)
        # print("")
        # input(str(x))
                
    print(len(text))