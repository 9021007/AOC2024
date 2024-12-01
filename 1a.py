with open('input.txt', 'r') as file:
    text = file.readlines()
    list1 = []
    list2 = []
    for i in range(len(text)):
        text[i] = text[i].strip()
        splittext = text[i].split("   ")
        list1.append(int(splittext[0]))
        list2.append(int(splittext[1]))
    # list1 = list(set(list1))
    # list2 = list(set(list2))
    list1.sort()
    list2.sort()
    print(list1)
    print(list2)
    distances = []
    for i in range(len(list1)):
        distances.append(abs(list1[i] - list2[i]))
    print(distances)
    sum = 0
    for i in distances:
        sum += i
    print(sum)
        