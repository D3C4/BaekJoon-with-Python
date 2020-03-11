N, K = map(int, input().split())
i = 1
cnt = 0
while i <= N:
    if not N%i:
        cnt += 1
        if cnt == K:
            print(i)
            break
    i += 1
else:
    print(0)