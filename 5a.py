with open('input.txt', 'r') as file:
    text = file.read()
    splinput = text.split('\n\n')
    rules = splinput[0].split('\n')
    updates = splinput[1].split('\n')
    # print(rules)
    # print(updates)
    sum = 0
    
    for update in updates:
        valid = True
        array = update.split(',')
        array = [int(x) for x in array]
        for rule in rules:
            before = int(rule.split("|")[0])
            after = int(rule.split("|")[1])
            if before in array and after in array:
                if array.index(before) < array.index(after):
                    pass
                else:
                    valid = False
        if valid:
            sum += array[int(len(array)/2)]
    print(sum)