word = input().lower()
char_list = {}
for c in word:
    if c not in char_list.keys():
        char_list[c] = 1
    else:
        char_list[c] += 1
tmp = sorted(char_list, key = lambda k : char_list[k])
if len(word) == 1:
    print(f"{word.upper()}")
elif char_list[tmp[-1]] == char_list[tmp[-2]]:
    print("?")
else:
    print(f"{tmp[-1].upper()}")