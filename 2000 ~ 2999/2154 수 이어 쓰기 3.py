n = input()
st = ''
a = 0
while True:
    a += 1
    for i in range(10 * (a - 1) + 1, 10 * a + 1):
        st += str(i)
    if(n in st):
        print(st.index(n) + 1)
        break