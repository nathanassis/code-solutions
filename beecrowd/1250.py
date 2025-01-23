n = int(input())

while n > 0:
	qt, t, s, cont = int(input()), list(map(int, input().split())), input(), 0
	
	for i in range(qt):
		if t[i] <= 2 and s[i] == 'S':
			cont += 1
		elif t[i] > 2 and s[i] == 'J':
			cont += 1
	
	print(cont)
	n -= 1
