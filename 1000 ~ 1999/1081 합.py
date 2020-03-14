l, u = map(int, input().split())
sum_n = 0
for i in range(l, u + 1):
    for j in set(str(i)):
        sum_n += int(j)
print(sum_n)