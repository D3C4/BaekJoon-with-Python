word = input()
letters = list(word)
dic = {}

for i in letters:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

sortedKeys = sorted(dic.keys())
oddCount = 0
oddLetter = ''

for i in sortedKeys:
    if dic[i] % 2 == 1:
        oddCount += 1
        oddLetter = i
        if oddCount >= 2:
            print("I'm Sorry Hansoo")
            break

if oddCount < 2:
    if oddLetter != '' and dic[oddLetter] == 1:
        sortedKeys.remove(oddLetter)

    for i in sortedKeys:
        print(i * int(dic[i] / 2), end = '')

    if oddLetter != '':
        print(oddLetter, end = '')

    for i in reversed(sortedKeys):
        print(i * int(dic[i] / 2), end = '')