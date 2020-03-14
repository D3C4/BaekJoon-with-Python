a, b, c = map(int, input().split())
i = 0
while True:
    i += 1
    if(a + b * 2  - c * 2 > a + b - c):
        print(-1)
        break
    else:
        print(int(a / (c - b)+ 1))
        break