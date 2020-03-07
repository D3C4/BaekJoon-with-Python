import sys

T = int(input())
for _ in range(T):
    f = [(1, 0), (0, 1)]
    n = int(input())
    if n == 0:
        for e in f[0]:
            print(e, end=" ")
        print()
    elif n == 1:
        for e in f[1]:
            print(e, end=" ")
        print()
    else:
        for i in range(n-1):
            f.append((f[i][0]+f[i+1][0], f[i][1]+f[i+1][1]))
        for e in f[n]:
            print(e, end=" ")
        print()