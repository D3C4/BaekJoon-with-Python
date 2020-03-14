import collections

lst = []
sumn = 0
for i in range(10):
    n = int(input())
    lst.append(n)
    sumn += n
c1 = collections.Counter(lst)
c1t = c1.most_common(1)
print(sumn // 10)
print(c1t[0][0])