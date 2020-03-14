max_num = 0
max_index = 0

for i in range(9):
    a = int(input())

    if (a > max_num):
        max_num = a
        max_index = i + 1

print('%d\n%d' % (max_num, max_index))