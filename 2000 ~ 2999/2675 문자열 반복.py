T = int(input())
for i in range(T):
    result = []
    RS = input().split(' ')
    R = int(RS[0])
    S = ' '.join(RS[1]).split(' ')
    for j in S:
        result.append(j*R)
    print(''.join(result))