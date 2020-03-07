while True:
    s = input()
    if(s == '#'):
        break
    sl = list(s)
    answer = 0
    for i in range(len(sl)):
        if(sl[i] == '-'):
            answer += 0
        elif(sl[i] == '\\'):
            answer += 8 ** (len(sl) - 1 - i)
        elif (sl[i] == '('):
            answer += 2 * (8 ** (len(sl) - 1 - i))
        elif (sl[i] == '@'):
            answer += 3 * (8 ** (len(sl) - 1 - i))
        elif (sl[i] == '?'):
            answer += 4 * (8 ** (len(sl) - 1 - i))
        elif (sl[i] == '>'):
            answer += 5 * (8 ** (len(sl) - 1 - i))
        elif (sl[i] == '&'):
            answer += 6 * (8 ** (len(sl) - 1 - i))
        elif (sl[i] == '%'):
            answer += 7 * (8 ** (len(sl) - 1 - i))
        else:
            answer -= 8 ** (len(sl) - 1 - i)

    print(answer)