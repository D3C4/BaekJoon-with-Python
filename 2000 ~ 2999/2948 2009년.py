import calendar

d, m = map(int, input().split())
weekday = calendar.weekday(2009, m, d)

if weekday == 0:
    print('Monday')
elif weekday == 1:
    print('Tuesday')
elif weekday == 2:
    print('Wednesday')
elif weekday == 3:
    print('Thursday')
elif weekday == 4:
    print('Friday')
elif weekday == 5:
    print('Saturday')
else:
    print('Sunday')