N = int(input())
init = {}
state = True
for _ in range(N):
    data = input()
    if data[0] not in init:
        init[data[0]] = 1
    else:
        init[data[0]] += 1
result = []
for key, value in init.items():
    if value >= 5:
        result.append(key)
result.sort()
if result:
    print(''.join(result))
else:
    print("PREDAJA")