def div(row_start, row_end, col_start, col_end, num):
    if r == row_start and c == col_start:
        print(num)
        return

    row_mid = (row_start + row_end) // 2
    col_mid = (col_start + col_end) // 2

    n = (row_mid - row_start) * (col_mid - col_start)

    if row_start <= r < row_mid and col_start <= c < col_mid: # 왼쪽 위
        div(row_start, row_mid, col_start, col_mid, num)
    elif row_start <= r < row_mid and col_mid <= c < col_end:  # 오른쪽 위
        div(row_start, row_mid, col_mid, col_end, num+n)
    elif row_mid <= r < row_end and col_start <= c < col_mid:  # 왼쪽 아래
        div(row_mid, row_end, col_start, col_mid, num+(n*2))
    elif row_mid <= r < row_end and col_mid <= c < col_end:  # 오른쪽 아래
        div(row_mid, row_end, col_mid, col_end, num+(n*3))

N, r, c = map(int, input().split())
pow_ = 1 << N
div(0, pow_, 0, pow_, 0)