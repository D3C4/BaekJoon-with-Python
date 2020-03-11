def fibonacci(n):
    base1, base2 = 0, 1
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        for i in range(n - 1):
            new_number = base1 + base2
            base1 = base2
            base2 = new_number
        return new_number

print(fibonacci(int(input())))