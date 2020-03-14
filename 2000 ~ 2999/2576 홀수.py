d = 0
sum  = 0
nums = list()
for i in range(7):
    num = int(input())
    if(num % 2 == 1):
        sum += num
        nums.append(num)
        d = 1
nums.sort()
if(d == 0):
    print('-1')
else:
    print(sum)
    print(nums[0])