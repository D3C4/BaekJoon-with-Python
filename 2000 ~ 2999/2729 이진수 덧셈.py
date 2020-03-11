for i in range(int(input())):
    n, k = map(str, input().split())
    print(str(bin(int(n, 2) + int(k, 2)))[2:])