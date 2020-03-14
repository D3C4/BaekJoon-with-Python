'''
def gcd(a, b):
    while(True):
        if b%a:
            temp = a
            a = b % a
            b = temp
        else:
            return a


def my_map(func, input_list):
    return [func(i) for i in input_list]


A, B = my_map(int, input().split())
for i in range(gcd(A, B)):
    print(1,end='')
'''

import math
a, b = map(int, input().split())
print(math.gcd(a, b))