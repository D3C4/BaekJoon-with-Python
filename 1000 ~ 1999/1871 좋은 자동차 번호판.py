N = int(input())
for i in range(N):
    score_front = 0
    LD = input().split('-')
    for j in range(3):
        score_front += (ord(LD[0][j]) - 65) * (26 ** (2-j))
    if(abs(score_front - int(LD[1])) <= 100):
        print('nice')
    else:
        print('not nice')