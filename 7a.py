from copy import deepcopy
from itertools import product

def solveLTR(inputString):
    inputString = inputString.split(" ")
    result = int(inputString[0])
    for i in range(1, len(inputString), 2):
        if inputString[i] == "+":
            result += int(inputString[i + 1])
        elif inputString[i] == "*":
            result *= int(inputString[i + 1])
    return result

with open('input.txt', 'r') as file:
    sum = 0
    text = file.readlines()
    for i in range(len(text)):
        possible = False
        text[i] = text[i].strip()
        target = text[i].split(": ")[0]
        eq = text[i].split(": ")[1].split(" ")
        operators = [' + ', ' * ']
        everycombo = list(product(operators, repeat=len(eq)))
        for j in range(len(everycombo)):
            neweq = deepcopy(eq)
            for k in range(len(eq) - 1):
                neweq.insert(2 * k + 1, everycombo[j][k])
            if int(solveLTR("".join(neweq))) == int(target):
                print("".join(neweq))
                possible = True
        if possible:
            sum += int(target)
    print(sum)