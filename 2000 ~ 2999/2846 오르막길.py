N = int(input())
arr = list(map(int, input().split()))
pre = arr[0]
max_h = 0
tmp = [arr[0]]
for h in arr[1:]:
    if(h > pre):
        tmp.append(h)
        pre = h
    elif(h <= pre):
        h_d = tmp[-1] - tmp[0]
        if(h_d > max_h):
            max_h = h_d
        tmp = [h]
    pre = h
if(len(tmp) >= 2):
    h_d = tmp[-1] - tmp[0]
    if(h_d > max_h):
        max_h = h_d
print(max_h)