while True:
	k = int(input())
	if k == 0:
		break
		
	n, m = map(int, input().split())
	
	while k > 0:
		x, y = map(int, input().split())
		
		if x == n or y == m:
			print("divisa")
		elif x > n and y > m:
			print("NE")
		elif x < n and y > m:
			print("NO")
		elif x > n and y < m:
			print("SE")
		else:
			print("SO")
		k -= 1