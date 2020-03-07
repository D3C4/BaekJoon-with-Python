import math

def primecheck(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


size = int(input())
num_list = list(map(int, input().split()))
count = 0
for i in num_list:
    if(primecheck(i) == True):
        count += 1

print(count)