train = 0
train_list = []
for i in range(4):
    a, b = map(int, input().split())
    train += b - a
    train_list.append(train)
print(max(train_list))