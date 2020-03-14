my_name = input()

max_prov = 0
choice = ""
same = []

my_L = my_name.count("L")
my_O = my_name.count("O")
my_V = my_name.count("V")
my_E = my_name.count("E")

for i in range(int(input())):
    her_name = input()

    her_L = her_name.count("L")
    her_O = her_name.count("O")
    her_V = her_name.count("V")
    her_E = her_name.count("E")

    provability = ((my_L + her_L + my_O + her_O) * (my_L + her_L + my_V + her_V) * (my_L + her_L + my_E + her_E) *
                   (my_O + her_O + my_V + her_V) * (my_O + her_O + my_E + her_E) * (my_V + her_V + my_E + her_E)) % 100

    if provability > max_prov:
        choice, max_prov = her_name, provability
        same.clear()
        same.append(choice)

    if provability == max_prov:
        same.append(her_name)

same.sort()
print(same[0])