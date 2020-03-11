def f2s(n):
    n = str(n).replace('5', '6', len(str(n)))
    return int(n)

def s2f(n):
    n = str(n).replace('6', '5', len(str(n)))
    return int(n)

originalA, originalB = map(str, input().split())
print(s2f(originalA) + s2f(originalB), f2s(originalA) + f2s(originalB))