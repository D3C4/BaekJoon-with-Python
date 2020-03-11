while True:
    a, b, c = input().split()
    a, c = int(a), int(c)
    if(a == 0 and b == 'W' and c == 0):
        break
    if b == 'W':
        if(a - c < -200):
            print("Not allowed")
        else:
            print(a - c)
    else:
        print(a + c)