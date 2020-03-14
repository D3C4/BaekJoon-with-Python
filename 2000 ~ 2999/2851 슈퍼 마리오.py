result = 0
for _ in range(10):
    mush = int(input())
    pre = result
    result += mush
    if result >= 100:
        break

if abs(100 - pre) == abs(100 - result):
    if pre > result:
        print(pre)
    else:
        print(result)
else:
    if abs(100 - pre) > abs(100 - result):
        print(result)
    else:
        print(pre)