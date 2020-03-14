T = int(input())
for i in range(T):
    print(list(sorted(list(map(int, input().split()))))[-3])