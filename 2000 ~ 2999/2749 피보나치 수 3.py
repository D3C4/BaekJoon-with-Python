num = int(input())
list = [0, 1]
for i in range(2, 1000000):
    list.append(list[i-1]+list[i-2])
    list[i] = list[i]%1000000
print(list[num % 1000000])