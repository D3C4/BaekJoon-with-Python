N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
while A:
    result += (A.pop(A.index(min(A)))*B.pop(B.index(max(B))))
print(result)