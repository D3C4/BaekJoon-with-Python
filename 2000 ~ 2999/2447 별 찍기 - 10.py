def r(n, i, j):
    global b
    if n == 1:
        g[i][j] = '*'
    else:
        for a in range(3):
            for b in range(3):
                if a != 1 or b != 1:
                    r(n//3, i+(n//3)*a, j+(n//3)*b)


N = int(input())
g = [[' ' for _ in range(N)] for _ in range(N)]
r(N, 0, 0)
for e in g:
    print(*e, sep='')