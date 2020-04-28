def gcd(a, b):
    return gcd(b % a, a) if b % a else a

def lcm(a, b):
    if a > b:
        a, b = b, a
    g = gcd(a, b)
    return (a * b) // g


A = list(map(int, input().split()))
B = list(map(int, input().split()))
l = lcm(A[1], B[1])
u = (A[0] * (l // A[1])) + (B[0] * (l // B[1]))
while True:
    g = gcd(l, u)
    if g == 1:
        break
    l //= g
    u //= g

print(u, l)