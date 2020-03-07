def checking(r, c, R, C):
    return r < 0 or r >= R or c < 0 or c >= C


def solution():
    R, C = map(int, input().split(' '))

    a1 = [[-1] * 770 for i in range(770)]
    a2 = [[-1] * 770 for i in range(770)]
    a3 = [[-1] * 770 for i in range(770)]
    a4 = [[-1] * 770 for i in range(770)]

    Map = []
    for i in range(R):
        Map.append(list(str(input())))

    for d in range(R + C + 1):
        for c in range(C):
            r = d - c
            if(checking(r, c, R, C)):
                continue
            if(checking(r + 1, c - 1, R, C)):
                a3[r][c] = (Map[r][c] == '1')
            else:
                a3[r][c] = (Map[r][c] == '1') * (a3[r+1][c-1] +1)

        for r in range(R):
            c = d - r
            if(checking(r, c, R, C)):
                continue
            if(checking(r - 1, c + 1, R, C)):
                a1[r][c] = (Map[r][c] == '1')
            else:
                a1[r][c] = (Map[r][c] == '1') * (a1[r-1][c+1] +1)

    for d in range(1-C, R):
        for r in range(R):
            c = r - d
            if(checking(r, c, R, C)):
                continue
            if(checking(r - 1, c - 1, R, C)):
                a4[r][c] = (Map[r][c] == '1')
            else:
                a4[r][c] = (Map[r][c] == '1') * (a4[r-1][c-1] +1)

        for r in range(R-1, -1, -1):
            c = r - d
            if(checking(r, c, R, C)):
                continue
            if(checking(r + 1, c + 1, R, C)):
                a2[r][c] = (Map[r][c] == '1')
            else:
                a2[r][c] = (Map[r][c] == '1') * (a2[r+1][c+1] +1)

    M = 0
    for r in range(R):
        for c in range(C):
            MP = min(a1[r][c], a2[r][c])
            if MP < M:
                continue
            for i in range(MP, 0, -1):
                if (c + 2 * (i - 1) >= C):
                    continue
                if (i < M):
                    break
                if min(a3[r][c+2*(i-1)], a4[r][c+2*(i-1)]) >= i:
                    M = max(M, i)
                    break
    print(M)


solution()