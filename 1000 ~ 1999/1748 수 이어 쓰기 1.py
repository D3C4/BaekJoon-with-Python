N = input()
len_N = len(N)
cnt = 0
for i in range(len_N-1):
    cnt += 9*10**i*(i+1)

print(cnt+(int(N) - 10**(len_N-1) + 1)*len_N)