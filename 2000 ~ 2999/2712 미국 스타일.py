for _ in range(int(input())):
    n, k = map(str, input().split())
    if(k == 'kg'):
        print('%.4f lb' % round(float(n) * 2.2046, 4))
    elif(k == 'lb'):
        print('%.4f kg' % round(float(n) * 0.4536, 4))
    elif(k == 'l'):
        print('%.4f g' % round(float(n) * 0.2642, 4))
    elif(k == 'g'):
        print('%.4f l' % round(float(n) * 3.7854, 4))