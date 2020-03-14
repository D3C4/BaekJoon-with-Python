import math

T = int(input())

for _ in range(T):
    N = int(input())
    primes = [False]+[False]+[True]*N
    for i in range(2, math.ceil(math.sqrt(N))):
        for j in range(i+i, N+1, i):
            primes[j] = False
    cnt_primes = {}
    for i in range(N+2):
        if primes[i]:
            while True:
                if N % i:
                    break
                else:
                    if i in cnt_primes:
                        cnt_primes[i] += 1
                    else:
                        cnt_primes[i] = 1
                    N //= i
    for key, value in cnt_primes.items():
        print(key, value)