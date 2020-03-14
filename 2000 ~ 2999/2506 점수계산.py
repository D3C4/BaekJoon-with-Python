n = int(input())
score = list(map(int, input().split()))
stack = 0
answer = 0
for i in range(n):
    if(score[i] == 1):
        stack += 1
        answer += stack
    else:
        stack = 0
print(answer)