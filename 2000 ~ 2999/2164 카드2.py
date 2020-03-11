import collections

c = collections.deque([i for i in range(1, int(input())+1)])
i = 0

while c.__len__() != 1:
    t = c.popleft()
    if i:
        c.append(t)
    i = (i+1)%2

print(c.popleft())