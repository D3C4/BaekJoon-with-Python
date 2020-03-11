result = []
for i in range(1, 6):
    if 'FBI' in input():
        result.append(str(i))
print(' '.join(result) if result else "HE GOT AWAY!")