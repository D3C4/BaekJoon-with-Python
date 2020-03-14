def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q = [v]
    visited = [False] * (N + 1)

    while q:
        v = q.pop(0)
        if not(visited[v]):
            visited[v] = True
            print(v, end=" ")
            for e in adj[v]:
                if not (visited[e]):
                    q.append(e)

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    a = input().split()
    adj[int(a[0])].append(int(a[1]))
    adj[int(a[1])].append(int(a[0]))

for e in adj:
    e.sort()

dfs(V)
print()
bfs(V)