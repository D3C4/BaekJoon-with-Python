size = int(input())
for i in range(size - 1):
    print(' ' * (size - i - 1) + '*' * (2 * i + 1))
print('*' * (2 * size - 1))
for i in range(size - 2, -1, -1):
    print(' ' * (size - i - 1) + '*' * (2 * i + 1))