def gcd(a, b):
    return gcd(b%a, a) if b%a else a

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b: a, b = b, a
    g = gcd(a, b)
    l = a * b // g
    print(l, g)