n, k = map(str, input().split())
if(int(n[::-1]) > int(k[::-1])):
    print(n[::-1])
else:
    print(k[::-1])