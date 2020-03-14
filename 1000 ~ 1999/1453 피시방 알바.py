n = int(input())
client = list(map(int, input().split()))
seat = [0 for i in range(100)]
count = 0
for i in range(n):
    if(seat[client[i] - 1] != 1):
        seat[client[i] - 1] = 1
    else:
        count += 1
print(count)