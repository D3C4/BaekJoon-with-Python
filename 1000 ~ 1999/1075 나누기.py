n = int(input())
f = int(input())
mn = n // 100 * 100
for i in range(100):
    if((mn + i) % f == 0):
        print('%02d' % i)
        break