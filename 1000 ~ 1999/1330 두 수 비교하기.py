numbers = input().split(' ')
if(int(numbers[0]) > int(numbers[1])):
    print('>')
elif(int(numbers[0]) < int(numbers[1])):
    print('<')
else:
    print('==')