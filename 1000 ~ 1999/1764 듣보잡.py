N, M = map(int, input().split())
a = set()
b = set()
for i in range(N):
    a.add(input())
for i in range(M):
    b.add(input())
l = list(a&b)
print(len(l))
for e in sorted(l):
    print(e)