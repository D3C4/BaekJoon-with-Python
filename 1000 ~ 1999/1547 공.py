tc = int(input())
bc = [1, 0, 0]
for i in range(tc):
    ab = input().split(' ')
    bc[int(ab[0]) - 1], bc[int(ab[1]) - 1] = bc[int(ab[1]) - 1], bc[int(ab[0]) - 1]
print(bc.index(1) + 1)