import string

for _ in range(int(input())):
    s1 = input()
    s2 = input()
    table = str.maketrans(s2, string.ascii_uppercase)
    s1 = s1.translate(table)
    print(s1)