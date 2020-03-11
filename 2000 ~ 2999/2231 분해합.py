N = int(input())
state = False

for i in range(1, N):
    bunhaehap = i
    i = str(i)
    for a in i:
        bunhaehap += int(a)
    if bunhaehap == N:
        state = True
        break
if state:
    print(i)
else:
    print(0)