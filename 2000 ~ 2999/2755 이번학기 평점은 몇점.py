total = 0
grade = 0
for i in range(int(input())):
    n, t, g = map(str, input().split())
    if (g == 'A+'):
        g = 4.3
    elif (g == 'A0'):
        g = 4.0
    elif (g == 'A-'):
        g = 3.7
    elif (g == 'B+'):
        g = 3.3
    elif (g == 'B0'):
        g = 3.0
    elif (g == 'B-'):
        g = 2.7
    elif (g == 'C+'):
        g = 2.3
    elif (g == 'C0'):
        g = 2.0
    elif (g == 'C-'):
        g = 1.7
    elif (g == 'D+'):
        g = 1.3
    elif (g == 'D0'):
        g = 1.0
    elif (g == 'D-'):
        g = 0.7
    elif (g == 'F'):
        g = 0.0
    total += int(t)
    grade += int(t) * g

print('%.2f' %round(grade / total, 2))