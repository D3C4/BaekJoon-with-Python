n_list = []

for i in range(int(input())):
    string = input()
    n = ""
    for j in range(len(string)):
        if string[j].isdecimal():
            n += string[j]
            if j == len(string) - 1:
                n_list.append(int(n))

        elif not string[j].isdecimal():
            if n == "":
                continue
            n_list.append(int(n))
            n = ""

n_list.sort()
for i in n_list:
    print(i)