point = [[0] * 101 for _ in range(101)]
cnt = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1+1, y2+1):
        for j in range(x1+1, x2+1):
            if not(point[j][i]):
                point[j][i] = 1
                cnt += 1
print(cnt)