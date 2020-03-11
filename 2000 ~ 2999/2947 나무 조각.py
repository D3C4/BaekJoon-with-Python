def sequence(series):
    seriesS = sorted(series)
    if(series[0] > series[1]):
        series[0], series[1] = series[1], series[0]
        for i in range(5):
            print(series[i], end = ' ')
        print('\n', end = '')
    if (series[1] > series[2]):
        series[1], series[2] = series[2], series[1]
        for i in range(5):
            print(series[i], end=' ')
        print('\n', end = '')
    if (series[2] > series[3]):
        series[2], series[3] = series[3], series[2]
        for i in range(5):
            print(series[i], end=' ')
        print('\n', end = '')
    if (series[3] > series[4]):
        series[3], series[4] = series[4], series[3]
        for i in range(5):
            print(series[i], end=' ')
        print('\n', end = '')
    if(series != seriesS):
        sequence(series)

group = input().split(' ')
for i in range(5):
    group[i] = int(group[i])
sequence(group)