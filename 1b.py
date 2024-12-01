with open('input.txt', 'r') as file:
    text = file.readlines()
    list1 = []
    list2 = []
    for i in range(len(text)):
        text[i] = text[i].strip()
        splittext = text[i].split("   ")
        list1.append(int(splittext[0]))
        list2.append(int(splittext[1]))

    scores = []

    for i in range(len(list1)):
        scores.append(list2.count(list1[i]) * list1[i])

    sum = 0
    for i in scores:
        sum += i

    print(sum)
        