def dfs(k, s):
    global r
    if s and int(s) <= N:
        r = max(r, int(s))

    if k == 7:
        return
    else:
        for n in '47':
            dfs(k + 1, s + n)


r = 0
N = int(input())
dfs(0, '')
print(r)