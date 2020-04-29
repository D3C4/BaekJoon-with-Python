N, K = int(input()), int(input())
s, e = 1, K

while s <= e:
    m = (s + e) // 2

    t = 0
    for i in range(1, N + 1):
        t += min(m // i, N)

    if t >= K:
        a = m
        e = m - 1
    else:
        s = m + 1

print(a)