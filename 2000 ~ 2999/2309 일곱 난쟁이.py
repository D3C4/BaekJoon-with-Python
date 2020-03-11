n = []
for i in range(9):
    n.append(int(input()))

n.sort()
total = sum(n)
tmp = []

flag = True
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if (total - n[i] - n[j]) == 100:
            for k in range(len(n)):
                if i == k or j == k:
                    continue
                print(n[k])
            flag = False
            break
    if flag == False:
        break