while True:
    space = 2
    nums = input()
    if(nums == '0'):
        break
    space += len(nums) - 1
    for _ in range(len(nums)):
        if(nums[_] == '1'):
            space += 2
        elif(nums[_] == '0'):
            space += 4
        else:
            space += 3
    print(space)