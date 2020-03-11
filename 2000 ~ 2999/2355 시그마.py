A, B = map(int, input().split())
if A > B:
    A, B = B, A
if A < 0 and B >= 0:
    n = abs(A)+B+1
elif A < 0 and B <= 0:
    n = abs(A-B)+1
elif A >= 0 and B >= 0:
    n = abs(B-A)+1

print(n*(A+B)//2)