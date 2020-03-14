length = int(input())
sequence = list()
for i in range(length):
    sequence.append(int(input()))
if(sequence[1] - sequence[0] == sequence[-1] - sequence[-2]):
    print(sequence[-1] + sequence[1] - sequence[0])
else:
    print(int(sequence[-1] * sequence[1] / sequence[0]))