import sys

N, L = map(int, sys.stdin.readline().split())

results = []
for length in range(L, 101):
    if length % 2 == 1:
        if N % length == 0:
            median = int(N / length)
            min_result = median - (length - 1) // 2
            if min_result < 0: break
            max_result = median + (length - 1) // 2
            for result in range(min_result, max_result+1):
                results.append(result)
            break

    elif length % 2 == 0: # 짝수
        value = N / length
        if (value - int(value)) == 0.5:
            min_result = int(value - 0.5) - (length // 2 - 1)
            if min_result < 0: break
            max_result = int(value + 0.5) + (length // 2 - 1)
            for result in range(min_result, max_result+1):
                results.append(result)
            break

if results:
    print(" ".join(map(str, results)))
else:
    print(-1)