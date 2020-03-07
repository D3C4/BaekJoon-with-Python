N = int(input())
for i in range(N):
    x, y = map(int, input().split(" "))
    i = 2
    if y - x == 1:
        cnt = 1
    elif y - x == 2:
        cnt = 2
    elif y - x == 3 or y -x == 4:
        cnt = 3
    else:
        while(True):
            if i**2 < (y - x) <= (i+1)**2:
                if ((i**2 + 1) + (i+1)**2)/2 <= (y - x) <= (i+1)**2:
                    cnt = 2*i+1
                else:
                    cnt = 2*i
                break
            else:
                i += 1
    print(cnt)