import collections
import sys

l = collections.deque(sys.stdin.readline()[:-1])
r = collections.deque()

lp = l.pop
la = l.append
le = l.extend
ra = r.appendleft
rp = r.popleft

for _ in range(int(sys.stdin.readline()[:-1])):
    c = sys.stdin.readline().split()

    if c[0] == 'L':
        if l:
            ra(lp())
    elif c[0] == 'D':
        if r:
            la(rp())
    elif c[0] == 'B':
        if l:
            lp()
    else:
        la(c[1])

le(r)
print(''.join(l))