import sys

N = int(input())
level = [int(input()) for _ in range(N)]
result = 0
for i in range(N-1, 0, -1):
    if level[i] <= level[i-1]:
        result += (level[i-1]-level[i]+1)
        level[i-1] = level[i]-1
print(result)