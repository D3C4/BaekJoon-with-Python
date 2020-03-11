n1 = int(input())
n2 = input()
for i in range(3):
    print(n1 * int(n2[-i-1]))
print(n1 * int(n2))