size = int(input())
for i in range(size - 1):
    print('*' * (i + 1) + ' ' * 2 * (size - i - 1) + '*' * (i + 1))
print('*' * 2 * size)
for i in range(size - 1):
    print('*' * (size - i - 1) + ' ' * 2 * (i + 1) + '*' * (size - i - 1))