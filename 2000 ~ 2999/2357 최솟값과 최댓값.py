n, m = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
for _ in range(m):
    a, b = map(int, input().split())
    snl = list(sorted(num_list[a-1:b]))
    print(snl[0], snl[-1])