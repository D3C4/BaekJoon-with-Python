N = input()

if len(N) == 1:
    R = str(int(N) + 1 if int(N) + 1 != 10 else 11)
elif len(N) % 2 == 0:
    A = N[:len(N) // 2]
    B = N[len(N) // 2:]
    if int(A[::-1]) > int(B):
        R = A + A[::-1]
    else:
        A = str(int(A) + 1)
        R = A + A[::-1]
else:
    A = N[:len(N) // 2]
    B = N[len(N) // 2 + 1:]
    C = N[len(N) // 2]
    if int(A[::-1]) > int(B):
        R = A + C + A[::-1]
    else:
        A = str(int(A) * 10 + int(C) + 1)
        R = A + A[-2::-1]

if len(N) + 2 == len(R):
    R = R[:len(R) //2 ] + R[len(R) // 2 + 1:]

print(R)


