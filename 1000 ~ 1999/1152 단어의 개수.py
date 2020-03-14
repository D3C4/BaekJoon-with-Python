s = input()
s_list = s.split(' ')
s_len = len(s_list)
if(s_list[0] == ''):
    s_len -= 1
if(s_list[-1] == ''):
    s_len -= 1
print(s_len)