N = int(input())
count = 0
i = 1
while True:
    count += 1
    N -= i
    if (N < 0):
        N += i
        i = 0
        count -= 1
    if (N == 0):
        break
    i += 1
print(count)