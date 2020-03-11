n = int(input())
stars = list()
for i in range(n - 1):
    stars.append(' ' * (n - i - 1) + '*' * (i + 1))
    print(' ' * (n - i - 1) + '*' * (i + 1))
print('*' * n)
for i in range(n - 1):
    print(list(reversed(stars))[i])