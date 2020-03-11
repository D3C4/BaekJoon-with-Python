size = int(input())
for i in range(size - 1):
    print('*' * (i + 1))
print('*' * size)
for i in range(size - 1, 0, -1):
    print('*' * i)