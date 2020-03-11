N = int(input())
c = [0, 1]
for i in range(2, N+1):
    c = [sum(c), c[0]]
print(sum(c))