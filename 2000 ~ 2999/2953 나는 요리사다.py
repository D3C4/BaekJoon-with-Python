cook = []
for i in range(5):
    cook.append(sum(map(int, input().split())))
print(cook.index(max(cook)) + 1, max(cook))