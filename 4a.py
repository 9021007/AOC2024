with open('input.txt', 'r') as file:
    text = file.readlines()
    text = [line.strip() for line in text]
    word = "XMAS"
    backword = "SAMX"
    count = 0
    for i in range(len(text)):
        count += text[i].count(word)
        count += text[i].count(backword)
    side = list(zip(*text))[::-1]
    for i in range(len(side)):
        joined = ''.join(side[i])
        count += joined.count(word)
        count += joined.count(backword)
    lean = []
    for i in range(len(text)):
        lean.append('0'*i + text[i] + '0'*(len(text)-i-1))
    leanrot = list(zip(*lean))[::-1]
    for i in range(len(leanrot)):
        joined = ''.join(leanrot[i])
        count += joined.count(word)
        count += joined.count(backword)
    lean = []
    for i in range(len(text)):
        lean.append('0'*(len(text)-i-1) + text[i] + '0'*i)
    leanrot = list(zip(*lean))[::-1]
    for i in range(len(leanrot)):
        joined = ''.join(leanrot[i])
        count += joined.count(word)
        count += joined.count(backword)

    print(count)
        