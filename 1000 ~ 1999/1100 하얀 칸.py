count = 0
for _ in range(8):
    tile = input()
    for __ in range(8):
        if(_ % 2 == 0 and __ % 2 == 0 and tile[__] == 'F'):
            count += 1
        elif(_ % 2 == 1 and __ % 2 == 1 and tile[__] == 'F'):
            count += 1
print(count)