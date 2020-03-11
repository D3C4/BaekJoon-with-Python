for i in range(int(input())):
    n, k = map(str,input().split())
    print(k[:int(n) - 1] + k[int(n):])