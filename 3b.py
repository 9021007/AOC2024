import re
with open('input.txt', 'r') as file:
        text = file.read()
        selections = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)', text)
        sum = 0
        enabled = True
        for i in range(len(selections)):
            if selections[i].startswith("do"):
                enabled = True
            if selections[i].startswith("don't"):
                enabled = False
            if selections[i].startswith("mul") and enabled:
                splittext = selections[i].split(",")
                splittext[0] = splittext[0].split("(")[1]
                splittext[1] = splittext[1].split(")")[0]
                sum += int(splittext[0]) * int(splittext[1])
        print(sum)