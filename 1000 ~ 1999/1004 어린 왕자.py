def check(source, destination, star_info):
    global cnt
    for e in star_info:
        if((source[0] - e[0]) ** 2 + (source[1] - e[1]) ** 2 < e[2] ** 2) ^ ((destination[0] - e[0]) ** 2 + (destination[1] - e[1]) ** 2 < e[2] ** 2):
            cnt += 1

T = int(input())
for _ in range(T):
    pos_info = list(map(int, input().split()))
    src = [pos_info[0], pos_info[1]]
    dst = [pos_info[2], pos_info[3]]
    n = int(input())
    cnt = 0
    star_info = [list(map(int, input().split())) for _ in range(n)]

    check(src, dst, star_info)
    print(cnt)