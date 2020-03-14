def f(i, j):
    global min_cnt
    check_color = ['B', 'W']
    for color in range(2):
        cnt = 0
        for ni in range(i, i+8):
            for nj in range(j, j+8):
                if board[ni][nj] != check_color[color%2]:
                    cnt += 1
                color += 1
            color += 1
        if cnt < min_cnt:
            min_cnt = cnt


N, M = map(int, input().split())
board = [input() for _ in range(N)]
min_cnt = 999999
for i in range(N-7):
    for j in range(M-7):
        f(i, j)
print(min_cnt)