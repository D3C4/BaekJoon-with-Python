M = int(input())
N = int(input())
result = []
for i in range(1,10001):
    if M <= i**2 <= N:
        result.append(i**2)
    elif i**2 > N:
        break
if result == []:
    print(-1)
else:
    print(f'{sum(result)}\n{result[0]}')