score = list()
score5 = list()
sum = 0
for i in range(8):
    score.append(int(input()))
for i in range(5):
    sum += list(sorted(score))[-i-1]
    score5.append(score.index(list(sorted(score))[-i-1]) + 1)
print(sum)
for i in range(5):
    print(list(sorted(score5))[i], end = ' ')