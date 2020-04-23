N, M = list(map(int, input().split()))

m1, m2, res = 100000, 100000, None
for i in range(M):
    res = list(map(int, input().split()))
    m1, m2 = min(m1, res[0]), min(m2, res[1])

if N > 6:
    rm, qt = N % 6, N // 6
    res = [m1 * ((qt) + 1), m1 * qt + m2 * rm, m2 * N]
    if rm * m2 > m1:
        res = min(res[0:2])
    else:
        res = min(res)
else:
    res = min(m1, m2 * N)

print(res)