ns = int(input())
ans_l = []
asc_nl = []

for _ in range(ns): ans_l.append(int(input()))

asc_nl = sorted(ans_l)
stack = []
result = []
cp_l = []
i = 0
for num in asc_nl:
    if stack and stack[-1] == ans_l[i]:
        try:
            while stack[-1] == ans_l[i]:
                cp_l.append(stack.pop())
                result.append('-')
                i += 1
        except:
            stack.append(num)
            result.append('+')
            continue
    stack.append(num)
    result.append('+')

for _ in range(len(ans_l) - i):
    cp_l.append(stack.pop())
    result.append('-')

if ans_l == cp_l:
    for i in result:
        print(i, end="\n")
else:
    print("NO")