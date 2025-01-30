while True:
	try:
		r1, x1, y1, r2, x2, y2 = map(int, input().split())
		
		aux1 = (x2 - x1) ** 2
		aux2 = (y2 - y1) ** 2
		
		if r2 + (aux1+aux2) ** 0.5 <= r1:
			print("RICO")
		else:
			print("MORTO")
	except EOFError:
		break
