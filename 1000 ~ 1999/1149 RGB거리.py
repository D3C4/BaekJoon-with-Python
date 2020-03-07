import sys

def dfs(k, pre, cur):
    if k == N:
        return 0

    if pre == cur:
        return 999999999

    if memo[k][cur] != 999999999:
        return memo[k][cur]

    for i in range(3):
        memo[k][cur] = min(memo[k][cur], cost[k][cur] + dfs(k+1, cur, i))

    return memo[k][cur]

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[999999999]*3 for _ in range(N)]

print(min(dfs(0, 1, 0), dfs(0, 0, 1), dfs(0, 0, 2)))