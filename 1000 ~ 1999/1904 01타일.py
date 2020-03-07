N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    a = [1, 2]
    N -= 2
    i = 0
    while i < N:
        a[0], a[1] = a[1], a[0]
        a[1] = sum(a) % 15746
        i += 1
    print(a[-1])