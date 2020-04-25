X = int(input())
stick = [64]
while sum(stick) > X:
    tmp = stick.pop()
    stick.append(tmp // 2)
    stick.append(tmp // 2)
    if sum(stick[:len(stick)-1]) >= X:
        stick.pop()
    if sum(stick[:len(stick)-1]) == X:
        break
print(len(stick))