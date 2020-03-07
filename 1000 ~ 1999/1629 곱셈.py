A, B, C = map(int, input().split())

def d(x, m):
    if m == 0:
        return 1
    elif m == 1:
        return x
    elif m % 2 > 0:
        return d(x, m-1)*x
    h = d(x, m // 2)
    h %= C
    return h**2 % C

print(d(A, B) % C)