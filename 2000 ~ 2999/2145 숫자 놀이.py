def change(n):
    sumn = 0
    lit_n = str(n)
    for i in lit_n:
        sumn += int(i)
    if(sumn < 10):
        return sumn
    else:
        return change(sumn)

while True:
    n = int(input())
    if(n == 0):
        break
    print(change(n))