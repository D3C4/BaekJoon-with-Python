num_list = list()
n = int(input())
for i in range(n):
    number = int(input())
    num_list.append(number)
num_list.sort()
for i in range(len(num_list)):
    print(num_list[i])