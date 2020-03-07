def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac

num = int(input())
i = 1
while True:
    if(str(factorial(num))[-i] != '0'):
        print(i - 1)
        break
    i += 1
