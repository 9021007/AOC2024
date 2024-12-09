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
    # print(''.join(fs))
    for i in tqdm(range(len(fs))):
        # print(i, fs[i])
        # print(len(fs))
        if fs[i] == ".":
            for j in range(len(fs)):
                if fs[len(fs) - j - 1] != ".":
                    fs[i] = fs[len(fs) - j - 1]
                    fs[len(fs) - j - 1] = "."
                    break
                
    # idk why i needed this, the last digit wasnt working :shrug:
    if fs[-1] != ".":
        for i in range(len(fs)):
            if fs[i] == ".":
                fs[i] = fs[-1]
                fs[-1] = "."
                break

    print(''.join(fs))

    sum = 0

    for i in range(len(fs)):
        if fs[i] != ".":
            sum += int(fs[i]) * i

    print(sum)