def lcm(a, b):
    d = gcd(a, b)
    return d * (a // d) * (b // d)


def gcd(a, b):
    return gcd(b % a, a) if b % a else a


T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))