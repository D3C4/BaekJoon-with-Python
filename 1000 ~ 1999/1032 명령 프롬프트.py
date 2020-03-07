N = int(input())
file_name = [input() for _ in range(N)]
result = ""
for e in zip(*file_name):
    if len(set(e)) == 1:
        result += e[0]
    else:
        result += '?'
print(result)