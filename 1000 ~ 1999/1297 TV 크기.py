C, B, A = map(int, input().split())
x = (C**2/(B**2+A**2))**0.5
print(int(B*x), int(A*x))