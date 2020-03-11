diary = input()
org = ""
stack = 0

for c in range(len(diary)):
    if stack:
        stack -= 1
        continue
    if diary[c] not in ['a', 'e', 'i', 'o', 'u']:
        org += diary[c]
    else:
        org += diary[c]
        stack = 2

print(org)