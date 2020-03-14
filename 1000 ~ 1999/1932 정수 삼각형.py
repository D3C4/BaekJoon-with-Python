import sys
N = int(sys.stdin.readline())
t = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(N - 1):
    for __ in range(len(t[_ + 1])):
        if(__ == 0):
            t[_ + 1][__] = t[_][__] + t[_ + 1][__]
        elif(__ == len(t[_ + 1]) - 1):
            t[_ + 1][-1] = t[_][-1] + t[_ + 1][-1]
        else:
            t[_ + 1][__] = max(t[_][__-1] + t[_ + 1][__], t[_][__] + t[_ + 1][__])

print(max(t[-1]))