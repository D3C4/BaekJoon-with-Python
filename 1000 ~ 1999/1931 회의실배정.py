import sys

N = int(sys.stdin.readline())
mt = []

for _ in range(N): mt.append(list(map(int, sys.stdin.readline().split())))

mt = sorted(mt, key=lambda x: [x[1], x[0]])

m_mt = 0
st = 0
for _ in mt:
    if _[0] >= st:
        st = _[1]
        m_mt += 1

print(m_mt)