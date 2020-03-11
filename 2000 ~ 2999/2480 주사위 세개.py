n = dict()
for a in map(int, input().split()):
    try:
        n[a] += 1
    except:
        n[a] = 1
if len(n) == 1:
    print(10000+sum(n.keys())*1000)
elif len(n) == 2:
    print(1000+sorted(n, key=lambda x: n[x])[1]*100)
elif len(n) == 3:
    print(sorted(n)[-1]*100)