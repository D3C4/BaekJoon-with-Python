a = ''
nk = list(map(int, input().split()))
for i in range(1, nk[0] + 1):
    a += str(i)

print(a)
if(nk[1] > len(a)):
    print(-1)
else:
    print(a[nk[1] - 1])