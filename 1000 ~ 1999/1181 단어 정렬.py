words = {}
result = []
N = int(input())
for i in range(N):
    word = input()
    if len(word) not in words:
        words[len(word)] = [word]
    else:
        if word not in words[len(word)]:
            words[len(word)].append(word)
for i in sorted(words.keys()):
    result += sorted(words[i])
for i in result:
    print(i)