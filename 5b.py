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
        for i in range(len(rules)):
            needsrepeat = False
            for rule in rules:
                before = int(rule.split("|")[0])
                after = int(rule.split("|")[1])
                if before in array and after in array:
                    if array.index(before) < array.index(after):
                        pass
                    else:
                        beforeindex = array.index(before)
                        afterindex = array.index(after)
                        array[beforeindex] = after
                        array[afterindex] = before
                        valid = False
                        needsrepeat = True
            if not needsrepeat:
                break
                
        if not valid:
            sum += array[int(len(array)/2)]
            # print(array)
            
    print(sum)