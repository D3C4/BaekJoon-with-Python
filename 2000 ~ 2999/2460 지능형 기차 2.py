people = 0
pl = []
for i in range(10):
    m, n = map(int, input().split())
    people += n - m
    pl.append(people)
print(max(pl))