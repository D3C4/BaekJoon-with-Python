for _ in range(int(input())):
    arr_size, idx = map(int, input().split())
    q = list(map(int, input().split()))
    chk = [0 for _ in range(arr_size)]
    chk[idx] = True

    cnt = 0
    while True:
        if q[0] == max(q):
            cnt += 1
            if chk[0]:
                print(cnt)
                break
            else:
                q.pop(0)
                chk.pop(0)
        else:
            q.append(q.pop(0))
            chk.append(chk.pop(0))