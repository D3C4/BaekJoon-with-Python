def room(n):
    result = 1
    for i in range(n):
        result += 6 * i
    return result


N = int(input())
i = 1
while (True):
    if room(i) >= N:
        print(i)
        break
    i += 1