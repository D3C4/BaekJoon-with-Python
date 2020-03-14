a, b = map(int, input().split())
min_price = 1000 / b * a
for i in range(int(input())):
    x, y = map(int, input().split())
    new = 1000 / y * x
    if(min_price > new):
        min_price = new

print('%.2f' % min_price)