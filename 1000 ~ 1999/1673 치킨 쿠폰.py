def chicken(n, k, s):
	if n == 0:
		return 0
	return n + chicken((n+s)//k, k, (n+s)%k)


while 1:
	try:
		n, k = map(int,input().split(' '))
	except:
		exit()
	print(chicken(n,k,0))