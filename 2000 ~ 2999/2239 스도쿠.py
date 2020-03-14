def 후보(pos):
    cell = [False] + [True for _ in range(9)]
    x = (pos[0]//3)*3
    y = (pos[1]//3)*3
    for _ in range(x, x+3):
        for __ in range(y, y+3):
            if puz[_][__]:
                cell[puz[_][__]] = False

    for _ in range(9):
        if puz[pos[0]][_]:
            cell[puz[pos[0]][_]] = False
        if puz[_][pos[1]]:
            cell[puz[_][pos[1]]] = False

    return [_ for _, __ in enumerate(cell) if __]


def 백트래킹(k):
    global state
    if k == len(zpt):
        for _ in puz:
            print(''.join(list(map(str, _))))
        state = True
    else:
        for num in 후보(zpt[k]):
            puz[zpt[k][0]][zpt[k][1]] = num
            백트래킹(k+1)
            if state:
                break
            puz[zpt[k][0]][zpt[k][1]] = 0


puz = []
zpt = []
state = False

for _ in range(9):
    row = list(map(int, list(input())))
    puz.append(row)
    for __ in range(9):
        if not row[__]:
            zpt.append([_, __])

백트래킹(0)