n = int(input())
loc = list(map(int, input().split()))
sum_n = 0

for i in range(n):
    for j in range(n):
        sum_n += abs(loc[i] - loc[j])

print(sum_n)