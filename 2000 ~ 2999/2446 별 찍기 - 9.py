n = int(input())
stars = list()
for i in range(n - 1):
    stars.append(' ' * (n - i - 2) + '*' * (2 * (i + 1) + 1))
stars = list(reversed(stars))
for i in range(len(stars)):
    print(stars[i])
print(' ' * (n - 1) + '*')
stars = list(reversed(stars))
for i in range(len(stars)):
    print(stars[i])