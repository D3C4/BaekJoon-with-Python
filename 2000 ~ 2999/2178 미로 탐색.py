def bfs(v):
    q = [v]
    lv = 0
    st = False
    while q:
        lv += 1
        for _ in range(len(q)):
            v = q.pop(0)
            if v == (N, M):
                st = True
                break
            if maze[v[0]][v[1]] == '1':
                maze[v[0]][v[1]] = '0'
                for a in range(4):
                    if maze[v[0] + di[a]][v[1] + dj[a]] == '1':
                        q.append((v[0] + di[a], v[1] + dj[a]))
        if st:
            break
    print(lv)
#h

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

N, M = map(int, input().split())
maze = [['0'] * (M + 2)] + [list('0' + input() + '0') for _ in range(N)] + [['0'] * (M + 2)]

bfs((1, 1))