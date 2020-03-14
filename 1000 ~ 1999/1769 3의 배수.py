n = input()
c = 0
if len(n) > 5:
    c += 1
    new = 0
    for i in n:
        new += int(i)
    n = new
else:
    n = int(n)

while len(str(n)) > 1:
    new = 0
    while n > 0:
        new += n % 10
        n //= 10
    n = new
    c += 1
print(c)
print(n % 3 == 0 and 'YES' or 'NO')