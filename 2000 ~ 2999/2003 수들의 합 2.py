N, M = map(int, input().split())
sums = [0]
s = 0
for n in input().split():
    s += int(n)
    sums.append(s)
cnt = 0
for i in range(len(sums)):
    if sums[i] >= M:
        for j in range(i):
            if sums[i] - sums[j] == M:
                cnt += 1

print(cnt)
