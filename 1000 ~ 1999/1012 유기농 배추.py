di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

def dfs(i, j):
    stack = [(i, j)]

    while(len(stack)):
        land[j][i] = 0
        for a in range(4):
            if land[j+dj[a]][i+di[a]]:
                stack.append((i, j))
                i+=di[a]
                j+=dj[a]
                break
        else:
            i, j = stack.pop()


T = int(input())
for tc in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    land = [[0]*(M+2) for i in range(N+2)]

    for k in range(K):
        i, j = map(int, input().split())
        land[j+1][i+1] = 1

    for j in range(N):
        j += 1
        for i in range(M):
            i += 1
            if land[j][i]:
                cnt += 1
                dfs(i, j)

    print(cnt)