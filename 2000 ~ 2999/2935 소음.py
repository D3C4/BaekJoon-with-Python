a = [0, 0, 0]
for i in range(3):
    a[i] = input()
if(a[1] == '+'):
    print(int(a[0]) + int(a[2]))
else:
    print(int(a[0]) * int(a[2]))