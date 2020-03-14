def n2s(s):
    r = []
    for c in s:
        if c == '0': r.append('zero')
        elif c == '1': r.append('one')
        elif c == '2': r.append('two')
        elif c == '3': r.append('three')
        elif c == '4': r.append('four')
        elif c == '5': r.append('five')
        elif c == '6': r.append('six')
        elif c == '7': r.append('seven')
        elif c == '8': r.append('eight')
        elif c == '9': r.append('nine')
    return ' '.join(r)

def s2n(s):
    s = s.split()
    r = []
    for c in s:
        if c == 'zero': r.append('0')
        elif c == 'one': r.append('1')
        elif c == 'two': r.append('2')
        elif c == 'three': r.append('3')
        elif c == 'four': r.append('4')
        elif c == 'five': r.append('5')
        elif c == 'six': r.append('6')
        elif c == 'seven': r.append('7')
        elif c == 'eight': r.append('8')
        elif c == 'nine': r.append('9')
    return ''.join(r)

M, N = map(int, input().split())
A = list(map(str, range(M, N+1)))
B = []
for n in A:
    B.append(n2s(n))
B.sort()
for i, s in enumerate(B, 1):
    print(s2n(s), end=' ')
    if i%10 == 0:
        print()