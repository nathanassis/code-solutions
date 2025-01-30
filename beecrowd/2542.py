while True:
	try:
		n = int(input())
		m, l = map(int, input().split())
		bm, bl = [], []
		
		for i in range(m):
			aux = (list(map(int, input().split())))
			bm.append(aux)
		
		for i in range(l):
			aux = (list(map(int, input().split())))
			bl.append(aux)
		
		cm, cl = map(int, input().split())
		a = int(input())
		
		if bm[cm-1][a-1] > bl[cl-1][a-1]:
			print("Marcos")
		elif bm[cm-1][a-1] < bl[cl-1][a-1]:
			print("Leonardo")
		else:
			print("Empate")
	except EOFError:
		break
