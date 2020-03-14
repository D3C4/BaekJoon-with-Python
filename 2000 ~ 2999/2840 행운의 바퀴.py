def check():
    for c in board:
        if not c: return False
    return True

N, K = map(int, input().split())
board = ['?']*N
alpha_check = [False]*26
work_stack = []
for _ in range(K):
    a, b = input().split()
    a = int(a)
    work_stack.append(a)
    work_stack.append(b)

i = 0
while work_stack:
    alpha = work_stack.pop()
    if board[i] == '?':
        if not alpha_check[ord(alpha)-ord('A')]:
            board[i] = alpha
            alpha_check[ord(alpha)-ord('A')] = True
        else:
            print('!')
            break
    else:
        if board[i] != alpha:
            print('!')
            break
    i += work_stack.pop()
    i %= N
else:
    print(*board, sep='')