N = int(input())
sequence = list(map(int, input().split()))

a, b = sequence[-1], sequence[-2]
count = 0

while True:
    count += 1
