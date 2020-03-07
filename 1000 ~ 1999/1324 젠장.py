def counting(a):
    max = 0
    c = 0
    for _ in a:
        if _ > max:
            max = _
            c += 1
    return c

quantity = int(input())
first = map(int, input().split())
second = map(int, input().split())
print(min(counting(first), counting(second)))