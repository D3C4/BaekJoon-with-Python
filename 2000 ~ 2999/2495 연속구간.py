def cnt(s):
    count = 1
    max_count = 1
    compare = s[0]

    for n in s[1:]:
        if n == compare:
            count += 1
        else:
            max_count = max(max_count, count)
            compare = n
            count = 1
    max_count = max(max_count, count)
    return max_count


for _ in range(3):
    print(cnt(input()))