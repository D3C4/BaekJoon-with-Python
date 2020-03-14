import sys
line, word = sys.stdin.read(), [0]*26
for s in line:
    if s.islower():
        word[ord(s)-97] += 1
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end='')