size = int(input())
yak = list(sorted(map(int, input().split())))
print(yak[0] * yak[-1])