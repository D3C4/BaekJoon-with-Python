N, M = map(int, input().split())
ss = [[0] for _ in range(N)]
for i in range(N):
    s = 0
    r = input().split()
    for j in range(M):
        s += int(r[j])
        ss[i].append(s)
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    s = 0
    for i in range(a-1, c):
        s += (ss[i][d]-ss[i][b-1])
    print(s)