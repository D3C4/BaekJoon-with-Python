T = int(input())

words = [input() for n in range(T)]

def checking(v):
    for i in range(len(v)):
        a = ['F', 'F']
        for j in range(i+1, len(v)):
            if(v[i] == v[j] and a[0] == 'T'): #비연, 독립
                a[1] = 'T'
            if(v[i] != v[j]): #비연
                a[0] = 'T'
            if(a[0] == 'T' and a[1] == 'T'): #둘 다 pass
                return 0
    return 1

count = 0
for word in words:
    count += checking(word)
print(count)