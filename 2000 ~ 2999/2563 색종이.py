paper = [[0]*101 for _ in range(101)]
N = int(input())
area = 0
for k in range(N):
    a, b = map(int, input().split())
    for i in range(b, b+10):
        for j in range(a, a+10):
            paper[i][j] = 1
for e in paper:
    for a in e:
        if a:
            area += 1
print(area)